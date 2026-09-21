# Trading Helper — сборка APK

## Вариант 1: GitHub Actions (без Linux)

1. Создай репозиторий на GitHub (Public)
2. Загрузи все файлы, сохранив структуру (особенно .github/workflows/build.yml)
3. Сборка запустится автоматически — вкладка Actions
4. Жди 30-60 минут
5. Скачай артефакт trading-helper-apk — внутри будет .apk

## Вариант 2: Linux / WSL2

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk autoconf libtool \
  pkg-config zlib1g-dev libncurses5-dev libffi-dev libssl-dev build-essential
pip install buildozer cython==0.29.34 setuptools
buildozer -v android debug
```

APK появится в папке bin/.

## Если сборка падает

1. Re-run: Actions -> Re-run failed jobs
2. Если падает на numpy/pandas — перезапусти, компиляция под ARM нестабильна
3. Память: сборка только arm64-v8a (одно архитектура) чтобы не падать по памяти
