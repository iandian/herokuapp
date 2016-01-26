  Dim path
  path = CreateObject("WScript.Shell").CurrentDirectory
  Dim oFSO : Set oFSO = CreateObject("Scripting.FileSystemObject")
  CopyFiles oFSO.GetFolder("F:\\Doc"), path & "\"  
  MsgBox("Finished! Check " & path) 


Sub CopyFiles(SourceFolder,DestFolderPath)
  Dim sFile, sSubFolder, dir, fso, totalFilesCount, piece, totalPiece, pieceCount
  set fso = CreateObject("scripting.FileSystemObject")

  totalFilesCount = SourceFolder.Files.Count
  piece = totalFilesCount / 100
  totalPiece = 0
  If piece < 1 Then
    piece = 1
  End If
  pieceCount = 0
  dir = DestFolderPath
  For Each sFile In SourceFolder.Files
    MsgBox(sFile.Path & " :DIR: " &dir & sFile.Name) 
	fso.copyfile sFile.Path, dir & sFile.Name , true
	pieceCount = pieceCount + 1
	If pieceCount = piece Then
	  pieceCount = 0
	  totalPiece = totalPiece + 1
	  If totalPiece < 100 Then
	    dir = dir & fso.GetBaseName(sFile) & "\"
	    fso.CreateFolder dir
      End If
	End If
  Next
  For Each sSubFolder In SourceFolder.SubFolders
    fso.CreateFolder DestFolderPath & sSubFolder.Name & "\"
    CopyFiles sSubFolder, DestFolderPath & sSubFolder.Name & "\"
  Next	
End Sub