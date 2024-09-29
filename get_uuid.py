import re


def extract_uuid_from_link(link: str) -> str | None:
    # Регулярное выражение для поиска UUID (формат 8-4-4-4-12)
    pattern = r"([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})"

    # Ищем соответствие по шаблону в ссылке
    match = re.search(pattern, link)

    if match:
        return match.group(0)  # Возвращаем найденный UUID
    return None  # Если UUID не найден



