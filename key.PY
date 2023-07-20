import tkinter as tk
from cryptography.fernet import Fernet

def generate_key():
    """Generate a new symmetric encryption key"""
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key)

def encrypt():
    """Encrypt a message using the shared key"""
    message = message_entry.get()
    key = key_entry.get().encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    result_entry.delete(0, tk.END)
    result_entry.insert(0, encrypted_message)

def decrypt():
    """Decrypt a message using the shared key"""
    encrypted_message = message_entry.get()
    key = key_entry.get().encode()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message.encode())
    result_entry.delete(0, tk.END)
    result_entry.insert(0, decrypted_message)

# Create the tkinter GUI
root = tk.Tk()
root.title("key Encryption")

# Key generation button
key_label = tk.Label(root, text="Shared Key:")
key_label.grid(row=0, column=0, padx=10, pady=10)
key_entry = tk.Entry(root, width=50)
key_entry.grid(row=0, column=1)
key_button = tk.Button(root, text="Generate Key", command=generate_key)
key_button.grid(row=0, column=2, padx=10, pady=10)

# Message input
message_label = tk.Label(root, text="Message:")
message_label.grid(row=1, column=0, padx=10, pady=10)
message_entry = tk.Entry(root, width=50 )
message_entry.grid(row=1, column=1)

# Encryption button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

# Decryption button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

# Result output
result_label = tk.Label(root, text="Result:")
result_label.grid(row=3, column=0, padx=10, pady=10)
result_entry = tk.Entry(root, width=50 )
result_entry.grid(row=3, column=1)

root.mainloop()
