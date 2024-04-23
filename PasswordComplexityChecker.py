def has_uppercase(password):
  """
  Checks if the password contains at least one uppercase letter.
  """
  return any(char.isupper() for char in password)

def has_lowercase(password):
  """
  Checks if the password contains at least one lowercase letter.
  """
  return any(char.islower() for char in password)

def has_number(password):
  """
  Checks if the password contains at least one number.
  """
  return any(char.isdigit() for char in password)

def has_special_char(password):
  """
  Checks if the password contains at least one special character.
  """
  special_chars = "!@#$%^&*()_+-=[]{};':,.<>/\?|"
  return any(char in special_chars for char in password)

def check_password_strength(password):
  """
  Evaluates the strength of a password based on various criteria.

  Args:
      password: The password to be assessed.

  Returns:
      A tuple containing:
          - strength (integer): A score representing password strength (higher is stronger).
          - feedback (string): Descriptive feedback about password strength.
  """
  strength = 0
  missing_criteria = []

  if len(password) >= 8:
    strength += 1
  else:
    missing_criteria.append("minimum length of 8 characters")

  if has_uppercase(password):
    strength += 1
  else:
    missing_criteria.append("at least one uppercase letter")

  if has_lowercase(password):
    strength += 1
  else:
    missing_criteria.append("at least one lowercase letter")

  if has_number(password):
    strength += 1
  else:
    missing_criteria.append("at least one number")

  if has_special_char(password):
    strength += 1
  else:
    missing_criteria.append("at least one special character")

  # Determine overall strength and feedback message
  if strength == 0:
    feedback = "This password is very weak. Please consider using a stronger password."
  elif strength == 1 or strength == 2:
    feedback = "This password is weak. It's recommended to add more complexity."
  elif strength == 3:
    feedback = "This password is moderately strong."
  else:
    feedback = "This password is strong!"

  return strength, feedback, missing_criteria

def main():
  """
  Prompts user for password and displays strength assessment until a strong password is entered.
  """
  is_strong = False
  while not is_strong:
    password = input("Enter your password: ")
    strength, feedback, missing_criteria = check_password_strength(password)
    print("strength of password is: ",strength)
    print(feedback)

    if strength >= 5:
      is_strong = True
    else:
      print("Your password is missing the following criteria for a strong password:")
      for criteria in missing_criteria:
        print("- " + criteria)

  print("Congratulations! You have entered a strong password.")
if __name__ == "__main__":
  main()