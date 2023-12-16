#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


def generate(filename, title, paragraph):
    """_summary_

    Args:
        filename (_type_): _description_
        title (_type_): _description_
        paragraph (_type_): _description_
    """
    styles = getSampleStyleSheet()
    print(styles.list())
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles['BodyText'])
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info])


if __name__ == "__main__":
    file = "processed.pdf"
    title = "A report on fruit store"
    paragraph = "Attached monthly report and fruit store update"
    generate(file, title, paragraph)
