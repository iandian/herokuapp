  Dim path
  path = CreateObject("WScript.Shell").CurrentDirectory
  Dim oFSO : Set oFSO = CreateObject("Scripting.FileSystemObject")
  CopyFiles oFSO.GetFolder("C:\\DPSearch\\TestData\\backup3"), path & "\"  
  MsgBox("Finished! Check " & path) 


Sub CopyFiles(SourceFolder,DestFolderPath)
  Dim sFile, sSubFolder, dir, fso, totalFilesCount, piece, totalPiece, pieceCount
  set fso = CreateObject("scripting.FileSystemObject")

  totalFilesCount = SourceFolder.Files.Count
  piece = CInt(totalFilesCount / 50)
  totalPiece = 0
  If piece < 1 Then
    piece = 1
  End If
  pieceCount = 0
  dir = DestFolderPath
  'WScript.Echo "Before: totalFilesCount:" & totalFilesCount & " piece: " & piece & " totalPiece: " & totalPiece & " pieceCount: " & pieceCount & " dir: " & dir
  For Each sFile In SourceFolder.Files
    'MsgBox(sFile.Path & " :DIR: " &dir & sFile.Name) 
	'On Error Resume Next
	fso.copyfile sFile.Path, dir & sFile.Name , true
	'If Err.Number <> 0 Then
      'MsgBox(sFile.Path & " :DIR: " &dir & sFile.Name) 
    'End If
	pieceCount = pieceCount + 1
	If pieceCount >= piece Then
	  pieceCount = 0
	  totalPiece = totalPiece + 1
	  If totalPiece < 50 Then
	    'dir = dir & fso.GetBaseName(sFile) & "\"
		dir = dir & totalPiece & "\"
	    fso.CreateFolder dir
      End If
	End If
	'WScript.Echo "In For Each: totalFilesCount:" & totalFilesCount & " piece: " & piece & " totalPiece: " & totalPiece & " pieceCount: " & pieceCount & " dir: " & dir
  Next
  For Each sSubFolder In SourceFolder.SubFolders
    fso.CreateFolder DestFolderPath & sSubFolder.Name & "\"
	'WScript.Echo "Print : sSubFolder:" & sSubFolder & " dest: " & DestFolderPath & sSubFolder.Name & "\" 
    CopyFiles sSubFolder, DestFolderPath & sSubFolder.Name & "\"
  Next	
End Sub