## keyz - 20

### Description

While webshells are nice, it'd be nice to be able to login directly. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. Make sure to copy it correctly! The key is in the ssh banner, displayed when you login remotely with ssh, to shell2017.picoctf.com.

### Hint

  - There are plenty of tutorials out there. This one covers key generation: https://confluence.atlassian.com/bitbucketserver/creating-ssh-keys-776639788.html
  - Then, use the web shell to copy/paste it, and use the appropriate tool to ssh to the server using your key

### Write up

On your webshell,

    ssh-keygen -t rsa -C "your_email@example.com"

then change public key name to `authorized_keys`, copy private key to your local station, login with it.

> who_needs_pwords_anyways
