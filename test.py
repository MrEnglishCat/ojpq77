from mimesis import Datetime, Text

print(Datetime(locale="ru").datetime().strftime('%Y-%m-%d_%H:%M'))
text = Text(locale="ru").text(quantity=1)
if len(text) > 50:
    print(f"{text[:47]}...")
else:
    print(f"{text}")
