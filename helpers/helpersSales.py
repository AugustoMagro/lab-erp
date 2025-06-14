from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SelectField, SubmitField, IntegerField, DateField, DecimalField
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch

PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
styles = getSampleStyleSheet()
listSales = []
total_price: float = 0

class SearchProductForm(FlaskForm):
    barcode = StringField('Barcode')
    name = StringField('Name')
    search = SubmitField('Search')

class AddProductForm(FlaskForm):
    amount = IntegerField('Amount')
    add = SubmitField('Add')

class SaleItem():
    def __init__(self, amount, id, barcode, name, unitPrice, price):
        self.amount = amount
        self.id = id
        self.barcode = barcode
        self.name = name
        self.unitPrice = unitPrice
        self.price = price

def go():
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    Story = [Spacer(1,0.5*inch)]
    style = styles["Normal"]

    insertParagraph(f"-"*20, 0.3,  style, Story)

    for sale in listSales:
        insertParagraph(f"{sale.amount} x {sale.name} ........... Unidade R$ {str(sale.unitPrice).replace('.',',')} - Total R$ {str(sale.price).replace('.',',')}", 0.3,  style, Story)

    insertParagraph(f"-"*20, 0.3, style, Story)
    insertParagraph(f"Total ........... R$ {sum([sale.price for sale in listSales])}", 0.3, style, Story)

    doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)
    buffer.seek(0)
    return buffer

def myFirstPage(canvas, doc):

    title = "ADEGA MV VINHOS E SUCOS"
    address = "RUA PADRE ANIBAL DIFRANCIA, 113, JARDIM MANGALOT, SÃO PAULO - SP"
    cnpj = "CNPJ: 100.100.100/0001-10"

    canvas.saveState()
    canvas.setFont('Times-Bold',10)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-50, title)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-70, address)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-90, cnpj)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "First Page / %s" % (doc.page))
    canvas.restoreState()

def myLaterPages(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch, "Page / %s" % (doc.page))
    canvas.restoreState()

def insertParagraph(text, space, style, story):
    bogustext = (text)
    p = Paragraph(bogustext, style)
    story.append(p)
    story.append(Spacer(1,space*inch))