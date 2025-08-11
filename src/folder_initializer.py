import os

def folderCreator():
  """
  Creates default folders for storing converted files based on their type (Images, Videos, Documents, Audio).
  These folders are created within a "Universal File Converter/Converted Files" directory.
  """

  # Base path
  base_path = "Universal File Converter/Converted Files"

  # Subfolders to create
  subfolders = ["Images", "Videos", "Documents", "Audio"]

  # Create each folder
  for subfolder in subfolders:
      folder_path = os.path.join(base_path, subfolder)
      os.makedirs(folder_path, exist_ok=True)
  print("Project folders created successfully.")