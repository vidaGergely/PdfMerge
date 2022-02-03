from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from PyPDF2 import PdfFileMerger

Builder.load_file("KV_files/pdf_merge.kv")
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilenames


class PdfMergeLayout(BoxLayout):
    readedPdfs = list()
    file_read_state = False

    def getBrowseWindow(self):
        self.ids["list_box"].text = ""
        Tk().withdraw()
        open_files = askopenfilenames(filetypes=[('pdf file', '*.pdf')])

        for open_file in open_files:
            self.readedPdfs.append(open_file)

        print(self.readedPdfs)

        for pdfs in self.readedPdfs:
            self.ids["list_box"].text += pdfs

        if len(self.readedPdfs) > 0:
            self.ids["merge_button"].disabled = False

    def mergePdf(self):

        print('MERGING...')
        merger = PdfFileMerger()
        for index, pdf in enumerate(self.readedPdfs, start=1):
            merger.append(pdf)
        Tk().withdraw()
        save_file = filedialog.asksaveasfilename(
            defaultextension='.pdf', filetypes=[("Pdf files", '*.pdf')],
            title="Choose filename")

        merger.write(save_file)
        merger.close()
        print('MERGING Success')
        self.readedPdfs = list()

        self.ids["list_box"].text = ""
        self.ids["merge_button"].disabled = True


class PdfMergeApp(App):
    def build(self):
        return PdfMergeLayout()


if __name__ == '__main__':
    PdfMergeApp().run()
