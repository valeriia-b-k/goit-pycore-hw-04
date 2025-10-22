# Скрипт створює окремий коміт для кожного нового або зміненого файлу
# і пропускає зображення (.png, .jpg, .svg)

$files = git status --porcelain | ForEach-Object { $_.Substring(3) }

foreach ($file in $files) {
    if ($file -match '\.(png|jpg|jpeg|svg)$') {
        Write-Host "⏭ Пропущено зображення: $file"
        continue
    }

    git add "$file"

    if ($file -match '\.py$') {
        $msg = "Add Python script $file"
    } elseif ($file -match '\.txt$') {
        $msg = "Add text file $file"
    } else {
        $msg = "Add file $file"
    }

    git commit -m "$msg"
    Write-Host "✅ Закомічено: $file"
}
