# data-security-lab
数据安全与隐私保护课程实验

## Experiment 1

Practice Git, GitHub, Codex and LaTeX. Test remote synchronization.

Run the demo: python code/demo.py

### English word frequency statistics

`code/text_stats.py` uses only the Python 3 standard library. Run it from the
repository root and pass the path to a UTF-8 text file:

```powershell
python code/text_stats.py sample.txt
```

Words are consecutive English letters (`[A-Za-z]+`), converted to lowercase.
Punctuation, numbers, and other characters act as separators. Results are sorted
by frequency descending, then alphabetically for ties. Paths containing spaces
should be enclosed in quotes.

The following test commands use PowerShell from the repository root.

#### 1. Normal input

```powershell
python code/text_stats.py sample.txt
```

Expected output (exit code `0`):

```text
Total words: 7
Unique words: 5
Word counts:
git: 2
hello: 2
and: 1
codex: 1
world: 1
```

#### 2. Empty file

Create a temporary empty file, run the program, and remove the temporary file:

```powershell
$emptyTestFile = [System.IO.Path]::GetTempFileName()
python code/text_stats.py "$emptyTestFile"
Remove-Item -LiteralPath $emptyTestFile
```

Expected output (exit code `0`):

```text
Total words: 0
Unique words: 0
Word counts:
(none)
```

Files containing no English words produce the same result.

#### 3. File not found

Generate a unique temporary path without creating a file:

```powershell
$missingTestFile = Join-Path ([System.IO.Path]::GetTempPath()) ([guid]::NewGuid().ToString() + '.txt')
python code/text_stats.py "$missingTestFile"
$LASTEXITCODE
```

Expected error on standard error (the actual generated path replaces `<path>`),
followed by exit code `1`:

```text
Error: file not found: <path>
1
```

Unreadable files and invalid UTF-8 input also produce an error and exit code `1`.
