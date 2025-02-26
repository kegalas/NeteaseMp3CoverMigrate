from mutagen.id3 import ID3, APIC
import shutil
import glob
import tkinter as tk
import os


def coverMigrate(path: str, save_new_file=True, keep_disc_img=True, label: tk.Label=None):
    mp3s = glob.glob(path+os.sep+"**"+os.sep+"*.mp3")
    for mp3 in mp3s:
        if label is not None:
            label.config(text=mp3.split(os.sep)[-1])
            label.update()

        new_path = mp3
        if save_new_file:
            new_path = mp3[:-4] + "_out.mp3"
            shutil.copy(mp3, new_path)

        audio = ID3(new_path)
        apic6 = None
        already_cover = False
        for apic in audio.getall("APIC"):
            if apic.type==6:
                apic6=apic
            if apic.type==3:
                already_cover = True

        if not keep_disc_img and already_cover:
            for key in list(audio.keys()):
                if key.startswith("APIC"):
                    apic_frame = audio.get(key)
                    if apic_frame.type == 6:
                        del audio[key]
            audio.save()
            continue

        if already_cover or apic6 is None:
            continue

        audio.add(
            APIC(
                encoding=apic6.encoding,
                mime=apic6.mime,
                type=3,
                desc='Cover',
                data=apic6.data
            )
        )
        audio.save()
