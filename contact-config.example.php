<?php
/**
 * Modèle de configuration du formulaire de contact.
 *
 * Copier ce fichier sous le nom `contact-config.php` sur le serveur, puis
 * y renseigner la clé. `contact-config.php` est exclu du dépôt : la clé
 * d'API ne doit jamais y figurer.
 */

return [
    // Clé d'API Resend, créée sur https://resend.com (tableau de bord,
    // « API Keys »). Droit d'envoi seulement.
    'cle_resend' => 'A_RENSEIGNER',

    // Expéditeur. Le domaine doit être vérifié dans Resend, sinon l'envoi
    // est refusé. Exemple : 'Amélie & Partners <site@amelie-invest.com>'.
    'expediteur' => 'Amélie & Partners <site@amelie-invest.com>',

    // Adresse qui reçoit les messages du formulaire.
    'destinataire' => 'contact@amelie-invest.com',
];
