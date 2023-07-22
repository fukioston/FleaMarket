
from django.db.transaction import atomic

from item.models import Items


@atomic
def load_model():
    with open('utils/datas.json', encoding="utf-8", errors="ignore") as fr:
        import json
        datas = json.load(fr)

        for data in datas:
            Items.objects.create(gname=data['gname'], userid=data['userid'], price=data['price'],
                                 intro_txt=data['intro_txt'], img_index=data['img_index'])

