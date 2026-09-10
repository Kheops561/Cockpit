<?php
/**
 * Réception du formulaire de contact.
 *
 * Le site reste un ensemble de fichiers statiques : ce script est le seul
 * composant serveur. Il est déposé à la racine, sur l'hébergement OVH, et
 * il envoie le message par l'API Resend.
 *
 * Conséquence importante : les pages du site n'appellent aucun domaine
 * tiers. Le navigateur ne parle qu'à amelie-invest.com ; c'est le serveur,
 * et lui seul, qui contacte Resend. La clé d'API ne quitte jamais le
 * serveur et ne figure pas dans le dépôt.
 *
 * Installation : voir INSTALLATION-FORMULAIRE.md.
 */

declare(strict_types=1);

const REPONSE_JSON = 'application/json; charset=utf-8';

// --------------------------------------------------------------- réglages
$config = __DIR__ . '/contact-config.php';
if (!is_file($config)) {
    repondre(500, 'Le formulaire n’est pas encore configuré sur le serveur.');
}
/** @var array $REGLAGES */
$REGLAGES = require $config;

// ------------------------------------------------------------- utilitaires
function veut_json(): bool
{
    $accept = $_SERVER['HTTP_ACCEPT'] ?? '';
    $ajax = $_SERVER['HTTP_X_REQUESTED_WITH'] ?? '';
    return str_contains($accept, 'application/json') || $ajax === 'fetch';
}

function repondre(int $code, string $message, bool $ok = false): never
{
    http_response_code($code);
    if (veut_json()) {
        header('Content-Type: ' . REPONSE_JSON);
        echo json_encode(['ok' => $ok, 'message' => $message], JSON_UNESCAPED_UNICODE);
        exit;
    }
    // Sans JavaScript : retour sur la page avec le résultat en paramètre.
    $etat = $ok ? 'ok' : 'erreur';
    header('Location: contact.html?envoi=' . $etat . '#formulaire');
    exit;
}

function champ(string $nom, int $max = 500): string
{
    $v = $_POST[$nom] ?? '';
    if (!is_string($v)) {
        return '';
    }
    // Les retours chariot isolés sont normalisés ; le reste est nettoyé des
    // caractères de contrôle, qui n'ont rien à faire dans un courrier.
    $v = str_replace(["\r\n", "\r"], "\n", $v);
    $v = preg_replace('/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/u', '', $v) ?? '';
    return mb_substr(trim($v), 0, $max);
}

// ------------------------------------------------------------ garde-fous
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    repondre(405, 'Méthode non autorisée.');
}

// Piège à robots : ce champ est masqué et doit rester vide. Aucun service
// extérieur n'est appelé pour cette vérification.
if (champ('site_web', 200) !== '') {
    // On répond « ok » sans rien envoyer : un robot ne doit pas apprendre
    // qu'il a été repéré.
    repondre(200, 'Message reçu.', true);
}

// Un formulaire rempli en moins de trois secondes n'a pas été rempli par
// une personne.
$pose = (int) ($_POST['pose'] ?? 0);
if ($pose > 0 && (time() - $pose) < 3) {
    repondre(200, 'Message reçu.', true);
}

// Limite simple par adresse : cinq envois par heure.
$ip = $_SERVER['REMOTE_ADDR'] ?? 'inconnue';
$piste = sys_get_temp_dir() . '/ap-contact-' . sha1($ip) . '.txt';
$envois = is_file($piste) ? array_filter(array_map('intval', file($piste))) : [];
$envois = array_values(array_filter($envois, static fn(int $t): bool => $t > time() - 3600));
if (count($envois) >= 5) {
    repondre(429, 'Trop de messages envoyés depuis cette connexion. Réessayez plus tard.');
}

// --------------------------------------------------------- les champs
$prenom   = champ('prenom', 80);
$nom      = champ('nom', 80);
$courriel = champ('courriel', 180);
$indicatif = champ('indicatif', 8);
$telephone = champ('telephone', 40);
$qualite  = champ('qualite', 60);
$profil   = champ('profil', 60);
$message  = champ('message', 5000);
$consent  = ($_POST['consentement'] ?? '') !== '';

$manques = [];
if ($prenom === '')   { $manques[] = 'le prénom'; }
if ($nom === '')      { $manques[] = 'le nom'; }
if ($courriel === '' || !filter_var($courriel, FILTER_VALIDATE_EMAIL)) { $manques[] = 'une adresse e-mail valide'; }
if ($qualite === '')  { $manques[] = 'à quel titre vous écrivez'; }
if ($profil === '')   { $manques[] = 'où vous en êtes'; }
if (mb_strlen($message) < 20) { $manques[] = 'quelques lignes sur votre situation'; }
if (!$consent)        { $manques[] = 'votre accord pour le traitement des informations'; }

if ($manques !== []) {
    repondre(422, 'Il manque ' . implode(', ', $manques) . '.');
}

// Les listes ne prennent que les valeurs proposées : on ne fait pas
// confiance à ce qui arrive.
$QUALITES = ['Particulier', 'Professionnel', 'Société (SCI, holding)', 'Autre'];
$PROFILS = ['Premier projet immobilier', 'Patrimoine déjà constitué',
            'Arbitrage ou refinancement', 'Autre'];
if (!in_array($qualite, $QUALITES, true)) { $qualite = 'Autre'; }
if (!in_array($profil, $PROFILS, true))   { $profil = 'Autre'; }

$tel = $telephone !== '' ? trim($indicatif . ' ' . $telephone) : 'non communiqué';

// ------------------------------------------------------------- le courrier
$sujet = 'Formulaire de contact · ' . $prenom . ' ' . $nom;
$texte = implode("\n", [
    'Prénom : ' . $prenom,
    'Nom : ' . $nom,
    'Adresse e-mail : ' . $courriel,
    'Téléphone : ' . $tel,
    'Vous êtes : ' . $qualite,
    'Où j’en suis : ' . $profil,
    '',
    'Message :',
    $message,
    '',
    '--',
    'Envoyé depuis le formulaire de contact d’amelie-invest.com le '
        . date('d/m/Y à H:i'),
]);

$charge = json_encode([
    'from'     => $REGLAGES['expediteur'],
    'to'       => [$REGLAGES['destinataire']],
    'reply_to' => $courriel,
    'subject'  => $sujet,
    'text'     => $texte,
], JSON_UNESCAPED_UNICODE);

$ch = curl_init('https://api.resend.com/emails');
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $charge,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT        => 15,
    CURLOPT_HTTPHEADER     => [
        'Authorization: Bearer ' . $REGLAGES['cle_resend'],
        'Content-Type: application/json',
    ],
]);
$retour = curl_exec($ch);
$code = (int) curl_getinfo($ch, CURLINFO_RESPONSE_CODE);
$erreur_curl = curl_error($ch);
curl_close($ch);

if ($retour === false || $code < 200 || $code >= 300) {
    // Le détail part dans le journal du serveur, jamais vers le visiteur :
    // il ne doit rien apprendre de la configuration.
    error_log('[contact] Resend a répondu ' . $code . ' ' . $erreur_curl . ' ' . (string) $retour);
    repondre(502, 'L’envoi a échoué. Réessayez dans un moment, ou écrivez directement à '
        . $REGLAGES['destinataire'] . '.');
}

$envois[] = time();
@file_put_contents($piste, implode("\n", $envois));

repondre(200, 'Message envoyé. Nous répondons sous un jour ouvré.', true);
