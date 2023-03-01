# Prompt the user to choose between creating a file or directory
$choice = Read-Host "Do you want to create a file or directory? Enter 'file' or 'directory'"

if ($choice -eq "file") {
    # If the user chose to create a file, prompt for the file path
    $filePath = Read-Host "Enter the path and name of the file you want to create (e.g. C:\path\to\file.txt)"

    # Use New-Item to create the file
    New-Item -ItemType File -Path $filePath
}
elseif ($choice -eq "directory") {
    # If the user chose to create a directory, prompt for the directory path
    $dirPath = Read-Host "Enter the path of the directory you want to create (e.g. C:\path\to\directory)"

    # Use New-Item to create the directory
    New-Item -ItemType Directory -Path $dirPath
}
else {
    # If the user entered an invalid choice, display an error message
    Write-Host "Invalid choice. Please enter 'file' or 'directory'."
}