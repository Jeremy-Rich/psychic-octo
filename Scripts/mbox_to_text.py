import mailbox
import os
from bs4 import BeautifulSoup

# Define output directories
output_dir = '/Users/jbear/Documents/psychic-octo/Scripts/Simon_mbox/output_texts'  # Directory to save email text files
attachments_dir = '/Users/jbear/Documents/psychic-octo/Scripts/Simon_mbox/attachments'  # Directory to save attachments

# Create directories if they don't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(attachments_dir):
    os.makedirs(attachments_dir)

# Function to save attachments
def save_attachment(part, email_number, output_dir):
    filename = part.get_filename()
    if filename:
        filepath = os.path.join(output_dir, f"{email_number}_{filename}")
        with open(filepath, 'wb') as f:
            f.write(part.get_payload(decode=True))
        return filepath
    return None

# Function to convert MBOX to text and save attachments
def mbox_to_text(mbox_file):
    mbox = mailbox.mbox(mbox_file)
    
    for i, message in enumerate(mbox):
        sender = message['from']
        date = message['date']
        subject = message['subject'][:50].replace(' ', '_') if message['subject'] else 'no_subject'
        
        # Construct filename using bear snake case convention
        filename = f"{sender}_EMAIL_{date[:10].replace('-', '_')}_{subject}.txt"
        filepath = os.path.join(output_dir, filename)

        # Extract email body
        if message.is_multipart():
            body = ''.join(part.get_payload(decode=True).decode(part.get_content_charset('utf-8'), 'ignore') 
                           for part in message.get_payload() if part.get_content_type() == 'text/plain')
        else:
            body = message.get_payload(decode=True).decode(message.get_content_charset('utf-8'), 'ignore')

        # Clean HTML if present
        soup = BeautifulSoup(body, 'html.parser')
        clean_text = soup.get_text()

        # Save email body
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(clean_text)

        # Save attachments
        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == 'application/octet-stream':
                    attachment_path = save_attachment(part, i + 1, attachments_dir)
                    if attachment_path:
                        with open(filepath, 'a', encoding='utf-8') as f:
                            f.write(f"\nAttachment: {attachment_path}")

# Usage
mbox_file_path = '/Volumes/BackUp Direct/Takeout 2/Mail/Simon_Rich.mbox'  # Update with the correct path
mbox_to_text(mbox_file_path)
