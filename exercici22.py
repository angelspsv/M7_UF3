# Exercici 22: crear una funció que retorni un fitxer XML
# la funció ha de crear les etiquetes i posar-hi text 
# s'ha de mostrar el fitxer per la consola 

import xml.etree.ElementTree as ET

def generar_xml():
    # per crear un fitxer XML s'utilitza la funció Element()
    p = ET.Element('students')

    # per crear subelements d'un element s'utilitza la funció 
    # subElement()
    c1 = ET.SubElement(p, 'student')
    # assignació d'un atribut i valor a l'element
    c1.set('type','regular')
    # creant childs de Student
    n = ET.SubElement(c1, 'name')
    n.text = "Angel"
    s = ET.SubElement(c1, 'surname')
    s.text = "Ivanov"
    m = ET.SubElement(c1, 'email')
    m.text = "angel@mail.com"
    d = ET.SubElement(c1, 'dni')
    d.text = "12345678X"


    c2 = ET.SubElement(p, 'student')
    c2.set('type','irregular')
    n = ET.SubElement(c2, 'name')
    n.text = "Marta"
    s = ET.SubElement(c2, 'surname')
    s.text = "Lopez"
    m = ET.SubElement(c2, 'email')
    m.text = "marta@mail.com"
    d = ET.SubElement(c2, 'dni')
    d.text = "98765432S"


    c3 = ET.SubElement(p, 'student')
    c3.set('type','regular')
    n = ET.SubElement(c3, 'name')
    n.text = "Daniel"
    s = ET.SubElement(c3, 'surname')
    s.text = "Marti"
    m = ET.SubElement(c3, 'email')
    m.text = "dani@mail.com"
    d = ET.SubElement(c3, 'dni')
    d.text = "45454587X"


    c4 = ET.SubElement(p, 'student')
    c4.set('type','irregular')
    n = ET.SubElement(c4, 'name')
    n.text = "Laura"
    s = ET.SubElement(c4, 'surname')
    s.text = "Rodriguez"
    m = ET.SubElement(c4, 'email')
    m.text = "laura@mail.com"
    d = ET.SubElement(c4, 'dni')
    d.text = "36985214M"


    # desarel XML creat
    tree = ET.ElementTree(p)
    tree.write("students.xml")

    # mostrar per la consola el xml
    ET.dump(p)

generar_xml()