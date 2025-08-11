def format_selector(destinationGroup):
  # Asking user to choose the output file format
  print("Select the format you would like to convert to: ")

  for i, extension in enumerate(destinationGroup):
    print(f"{i+1}. {extension}")

  selectedFormatIndex = int(input("\nSelect an option [number]: "))

  selectedFormat = destinationGroup[selectedFormatIndex - 1]
  print(f"Selected format: {selectedFormat}")
  return selectedFormat

  # Limit input to digits only and also 1 to 7 only nothing else