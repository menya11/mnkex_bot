# Как мы ведём ветки

Повседневная работа идёт в `develop`. Туда можно коммитить напрямую. Отдельная ветка под задачу допустима: она вливается в `develop`.

`main` — только выпущенный код. Туда попадает релиз:

1. Открыть pull request из `develop` в `main`.
2. Дождаться зелёного check `release-from-develop`.
3. Слить merge commit'ом.

Прямой push в `main` запрещён. Pull request в `main` из любой ветки, кроме `develop`, check отклоняет.

## Что включает владелец репозитория

У `akm77` нет прав admin, поэтому защиту веток включает `menya11`.

На приватном репозитории личного аккаунта защита доступна, если у владельца GitHub Pro. Иначе репозиторий нужно сделать публичным или перенести туда, где защита приватных веток есть.

1. Default branch → `develop`.
2. Защита ветки `main`:
   - require a pull request before merging;
   - approving reviews: 0;
   - required status check: `release-from-develop`;
   - block force pushes;
   - restrict deletions;
   - do not allow bypassing, включая администраторов.
3. `develop` не защищаем: в неё пушат напрямую.

Пока эти настройки не сохранены, GitHub прямой push в `main` не отклоняет. Check на pull request только помечает чужую ветку красным и сам по себе merge не блокирует.
