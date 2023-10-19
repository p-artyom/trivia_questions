from django.conf import settings


def cut_string(
    field: str,
    cut_out: int = settings.STR_LENGTH_WHEN_PRINTING_MODEL,
) -> str:
    '''Обрезает строку, если она больше заданной длины.

    Args:
        field: Текст строки.
        cut_out: Длина строки.

    Returns:
        Текст строки с добавлением многоточия, если он больше заданной длины.
    '''
    return field[:cut_out] + '…' if len(field) > cut_out else field
