CREATE TABLE Google_Vault_Records (
    email_recipient VARCHAR(255) NOT NULL,
    email_subject VARCHAR(512),
    email_sender VARCHAR(255) NOT NULL,
    record_id SERIAL PRIMARY KEY,
    date_sent TIMESTAMP NOT NULL
);
