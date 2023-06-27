#!/bin/bash

# Password length
password_length=12

# Generate random password
random_password=$(openssl rand -base64 48 | cut -c1-"$password_length")

echo "Generated password: $random_password"
