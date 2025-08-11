# detecting file extension
def extensionDetector(input_path):
  """
  This function takes the input file path and returns the file extension
  """
  splittedPath = input_path.split(".")
  inputFileExtension = splittedPath[1]
  return splittedPath, inputFileExtension


# Helper Functions
def groupify(fileGroups, inputFileExtension, group):
  """
  This function takes the input file extension and group and creates
  the suitable destination file extension list
  """
  destinationGroup = fileGroups[group].copy()
  destinationGroup.remove(inputFileExtension)
  return destinationGroup

def mapExtensions(fileGroups, inputFileExtension):
  """
  This function takes the input file extension and group and creates
  the suitable destination file extension list
  """
  group = ""
  destinationGroup = ""
  if inputFileExtension in fileGroups['image']:
    inputGroup = "image"
    destinationGroup = groupify(fileGroups, inputFileExtension, inputGroup)
  elif inputFileExtension in fileGroups['document']:
    inputGroup = "document"
    destinationGroup = groupify(fileGroups, inputFileExtension, inputGroup)
  elif inputFileExtension in fileGroups['audio']:
    inputGroup = "audio"
    destinationGroup = groupify(fileGroups, inputFileExtension, inputGroup)
  elif inputFileExtension in fileGroups['video']:
    inputGroup = "video"
    destinationGroup = groupify(fileGroups, inputFileExtension, inputGroup)
  else:
    print("File type not supported.")

  print(f"Group: {inputGroup}")
  print(f"Destination Group: {destinationGroup}")

  return inputGroup, destinationGroup

def call_extension_tool(inputFileExtension):

