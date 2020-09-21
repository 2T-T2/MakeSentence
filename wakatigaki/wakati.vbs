Option Explicit

Dim inputFilePath
inputFilePath = "テキストファイルパス"
Dim outputFilePath
outputFilePath = "wakati.csv"

Dim fso
Set fso = WScript.CreateObject("Scripting.FileSystemObject")

Dim doc
Set doc = CreateObject("Word.Application").Documents.Add()
Dim rng
Set rng = doc.Paragraphs(1).Range

Dim inputFile
Set inputFile = fso.OpenTextFile(inputFilePath,1,False,0)
Dim outputFile
Set outputFile = fso.OpenTextFile(outputFilePath,2,True)

Dim inputText
Do Until inputFile.AtEndOfStream
	inputText = inputText & inputFile.ReadLine
Loop

rng.Text = inputText

Dim wrd
Dim aryWrd()
Dim i
i = 0
For Each wrd In rng.Words
    ReDim Preserve aryWrd(i)
    aryWrd(i) = wrd.Text
    i = i + 1
Next

doc.Close False
Set doc = Nothing

Dim outputText
outputText = Join(aryWrd,",")
outputText = Replace(outputText,"。","。" & vbCrLf)
outputText = Replace(outputText, vbCrLf & ",", vbCrLf)

outputFile.WriteLine outputText

inputFile.Close
outputFile.Close