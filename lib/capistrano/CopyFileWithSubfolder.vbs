If Is64BitOS() Then
   Dim WshShell, bKeyEMCinstall, bKeyCommonFiles, dir, filePath
   dir = CreateObject("WScript.Shell").CurrentDirectory
   filePath = dir & "\" & Minute(now()) & Second(now()) & ".txt"
   Set WshShell = WScript.CreateObject("WScript.Shell")
   bKeyEMCinstall = WshShell.RegRead("HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\EMC\SourceOne\InstallDir")
   bKeyCommonFiles = WshShell.RegRead("HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\CommonFilesDir (x86)")
   Dim oFSO : Set oFSO = CreateObject("Scripting.FileSystemObject")
   Dim GiveVersionNo
   GiveVersionNo = InputBox("Enter VersionNo:")
   PrintDLLVersions oFSO.GetFolder(bKeyEMCinstall),GiveVersionNo,filePath  
   PrintDLLVersions oFSO.GetFolder(bKeyCommonFiles & "\EMC"),GiveVersionNo,filePath 
   MsgBox("Finished! Check " & filePath) 
End If




Function Is32BitOS()
    Const Path = "winmgmts:root\cimv2:Win32_Processor='cpu0'"
    Is32BitOS = (GetObject(Path).AddressWidth = 32)
End Function

Function Is64BitOS()
    Const Path = "winmgmts:root\cimv2:Win32_Processor='cpu0'"
    Is64BitOS = (GetObject(Path).AddressWidth = 64)
End Function

Function IsSameVersion(FileVersionNo,GiveVersionNo)
    IsSameVersion = StrComp(FileVersionNo,GiveVersionNo)       
End Function 

'Function TruncLeftZeros(string)
    'dim stringsa, stringsb
    'stringsa = Split(FileVersionNo,".");
    'stringsb = Split(GiveVersionNo,".");        
'End Function

Sub CopyFiles(Folder,FilePath)
  Dim oFile, oSubFolder, tempstr, fso, ts
  set fso = CreateObject("scripting.FileSystemObject")

  For Each oFile In Folder.Files
    tempstr = UCase(oFSO.GetExtensionName(oFile))
    If tempstr = "DLL" OR tempstr = "EXE" Then
      If(IsSameVersion(oFSO.GetFileVersion(oFile),VersionNo)<>0) Then
         tf.WriteLine(oFile.Path & vbTab & oFSO.GetFileVersion(oFile))
      End If
    End If
  Next
  tf.Close

  ' Scan the Folder's subfolders
  For Each oSubFolder In Folder.SubFolders
    PrintDLLVersions oSubFolder, VersionNo ,FilePath
  Next
End Sub

Sub PrintDLLVersions(Folder,VersionNo,FilePath)
  Dim oFile, oSubFolder, tempstr, fso, ts
  Const ForAppending = 8
  set fso = CreateObject("scripting.FileSystemObject")
  set tf = fso.OpenTextFile(FilePath, ForAppending, True)

  ' Scan the DLLs in the Folder
  For Each oFile In Folder.Files
    tempstr = UCase(oFSO.GetExtensionName(oFile))
    If tempstr = "DLL" OR tempstr = "EXE" Then
      If(IsSameVersion(oFSO.GetFileVersion(oFile),VersionNo)<>0) Then
         tf.WriteLine(oFile.Path & vbTab & oFSO.GetFileVersion(oFile))
      End If
    End If
  Next
  tf.Close

  ' Scan the Folder's subfolders
  For Each oSubFolder In Folder.SubFolders
    PrintDLLVersions oSubFolder, VersionNo ,FilePath
  Next
End Sub

Dim fso
Set fso = CreateObject("scripting.filesystemobject")

pt1 = "C:\TestFile\Test\" & a & "\"
total = root.files.length
if total > 100
#for each file in root.files
for a = 1 To total
    piece = total / 100
    pt1 = pt1 & file.name & "\"
    fso.CreateFolder pt1
	for b = 1 To piece
	  fso.copyfile file.name, pt1 & file.name,true
	next
next
if total < 100
for a = 1 To total
    pt1 = pt1 & file.name & "\"
    fso.CreateFolder pt1
	fso.copyfile file.name, pt1 & file.name,true
next

for each folder in root.folders
  copyfile
  through folder
next
For a = 1 To 299
pt1 = "C:\TestFile\Test\" & a & "\"
fso.CreateFolder pt1
fso.copyfile "c:\kk.txt", pt1 & a & ".txt",true
Next