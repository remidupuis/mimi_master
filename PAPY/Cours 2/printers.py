from textwrap import wrap

ZEN="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


COLOR = {
    "HEADER": "\033[95m",
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDC": "\033[0m",
}

class Printer:
    printers_system = []
    papers_system = {f'A{i}':200//(2**i) for i in range(0,6)}

    def __init__(self, avail_paper = [], printer_name = f'Printer {len(printers_system)}'):
        self.avail_paper = avail_paper
        self.printer_name = printer_name
        Printer.printers_system.append(self)
    
    @property
    def printer_name(self):
        return self._printer_name
    
    @printer_name.setter
    def printer_name(self, new_printer_name):
        if new_printer_name in [printer.printer_name for printer in Printer.printers_system]:
            raise ValueError(f'We already have a printer named {new_printer_name}')
        else:
            self._printer_name = new_printer_name
    @property
    def avail_paper(self):
        return self._avail_paper
    
    @avail_paper.setter
    def avail_paper(self, new_avail_paper):
        valid_paper = []
        invalid_paper = []
        for paper in new_avail_paper:
            if paper in Printer.papers_system:
                valid_paper.append(paper)
            else:
                invalid_paper.append(paper)
        if invalid_paper:
            print(f'Some formats are incorrect :{invalid_paper}')
        self._avail_paper = valid_paper

    def __repr__(self) -> str:
        return f' \n \n Printer name: {self.printer_name} \n Printer avail papers: {self.avail_paper}'

    def send(self, text, format = 'A4'):
        if format not in self.avail_paper:
            print(f'Format not available, this printer has the formats {self.avail_paper}')
        else:
            print("#"*Printer.papers_system[format])
            wrapped_text = wrap(text, width = Printer.papers_system[format])
            for line in wrapped_text:
                print(line)
            print("#"*Printer.papers_system[format])


class CollorPrinter(Printer):
    def send(self, text, format = 'A4', collor = 'GREEN'):
        print("", COLOR[collor])
        super().send(text, format)
        print("", COLOR['ENDC'])


if __name__ == '__main__':
    remi = Printer(avail_paper =['A4'], printer_name = 'Printer remi')
    Rodrigo = CollorPrinter(avail_paper =['A2', 'B3', 'A1'])
    Rodrigo.send(ZEN, format = 'A1', collor = 'RED')
    print(Printer.printers_system)
    

    

