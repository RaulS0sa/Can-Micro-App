#############################################################33
###
###         Good Reference: https://stackoverflow.com/questions/34276663/tkinter-gui-layout-using-frames-and-grid
###
################################################################
import json
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
global row_lef_side
row_lef_side = 0
global Lista_DEXX
global vops
Lista_DEXX = []
import xml.etree.ElementTree
import diag_new
import cantools
import can
import os
import io
import shutil

import numpy as np
#import thread
from threading import Thread
import stat
import time
global vops_name_context
vops_name_context = ""
global list_de_botones
global lista_de_entrys
lista_de_entrys = []

vops = diag_new.VOPS_interface()
global Label_config_return
global Label_config_return2
#vops.did_DE00.data = [0,0,0,0,0,0,0,0]
#vops.did_DE01.data = [0,0,0,0,0,0,0,0]
#print vops.did_DE00.data
global bus
global arreglo_sombo_boxes
arreglo_sombo_boxes = []

class Current_Message_type:
    def __init__(self):
        self.Message_name = ""
        self.Periodo_escrito = StringVar()
        self.Perido_contador = 0
        self.Value_send = IntVar()
        self.values_array_Check_box = []
        self.byte_array = []
        self.Index_of_array = 0
        self.generic_signal_info = []
        self.List_of_Messages_index = 0
class Second_screen_info:
    def __init__(self):
        self.Signal_name = ""
        self.array_index = 0
        self.Selection_value = 0
        self.is_continous = False
        self._unit = ""
        self.Valor_escrito_senal = StringVar()

class Text2_specify(Frame):
    def __init__(self, master, width=0, height=0, **kwargs):
        self.width = width
        self.height = height

        Frame.__init__(self, master, width=self.width, height=self.height)
        self.text_widget = Text(self, **kwargs)
        self.text_widget.pack(expand=YES, fill=BOTH)

    def pack(self, *args, **kwargs):
        Frame.pack(self, *args, **kwargs)
        self.pack_propagate(False)

    def grid(self, *args, **kwargs):
        Frame.grid(self, *args, **kwargs)
        self.grid_propagate(False)

class reader(Thread):
    def __init__(self):
        super(reader, self).__init__()
        ECUTxID = 0x728
        ECURxID = 0x720
        FDiagID = 0x7DF
        global bus

    def run(self):
        global Arrleglo_de_senales
        print(can.detect_available_configs())
        print(can.detect_available_configs(interfaces=['vector']))
        global bus
        print(can.interface.detect_available_configs())
        global Label_config_return
        global texto_botton_send_signal
        contador_1 = 0
        while True:
            try:
                # for msg in bus:
                #     print("{X}: {}".format(msg.arbitration_id, msg.data))


                n = 2

                for new_msg in bus:
                    if new_msg.arbitration_id == 1832:
                        cadena_de_texto = ''.join('{:02x}'.format(x) for x in new_msg.data)
                        arreglo = [cadena_de_texto[i:i + n] for i in range(0, len(cadena_de_texto), n)]
                        #print arreglo
                        if(arreglo[3] == 'de'):
                            print(arreglo)
                            contador_1 = 1
                            Label_config_return['text'] = str(arreglo[3]) + "" + str(arreglo[4]) + "= "+ str(arreglo[5]) + " "+ str(arreglo[6]) + " " +  str(arreglo[7]) + " "
                        elif (contador_1 == 1):
                            print(arreglo)
                            contador_1 = 0
                            Label_config_return2['text'] = str(arreglo[1]) + " " + str(arreglo[2]) + " " + str(arreglo[3]) + " " + str(arreglo[4]) + " " + str(arreglo[5]) + " " + str(arreglo[6]) + " " + str(arreglo[7]) + " "




                        #print type(new_msg.data)
                        #print str(new_msg.arbitration_id) + " " + str(new_msg.data)
                #notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])



            except Exception as ex:
                print (str(ex))
                pass
            #time.sleep(0.5)




class waiter(Thread):
    def __init__(self):
        super(waiter, self).__init__()
        ECUTxID = 0x728
        ECURxID = 0x720
        FDiagID = 0x7DF
        global bus
        bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, bitrate=500000)
        mensaje1 =can.Message(arbitration_id=2015,
                      data=[int(0x02), int(0x3E), int(0x80), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00)], extended_id=False)
        #self.Send_specific_messaje(mensaje1, 2)
        bus.send_periodic(mensaje1, period=500)
        time.sleep(0.1)
        diag_start = can.Message(arbitration_id=1824,
                      data=[int(0x02), int(0x10), int(0x03), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00)], extended_id=False)
        self.Send_specific_messaje(diag_start, 0)
        #bus.send_periodic(diag_start, period=500)
        time.sleep(0.15)
        diag_start1 = can.Message(arbitration_id=1824,
                                 data=[int(0x02), int(0x27), int(0x03), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00)], extended_id=False)
        self.Send_specific_messaje(diag_start1, 0)
        #bus.send_periodic(diag_start1, period=500)
        time.sleep(0.15)
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x30), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00)], extended_id=False)
        self.Send_specific_messaje(diag_start2, 0)
        #bus.send_periodic(diag_start2, period=500)
        time.sleep(0.15)
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x12), int(0x27), int(0x04), int(0x00), int(0x00), int(0x00), int(0x00)], extended_id=False)
        self.Send_specific_messaje(diag_start2, 0)
        #bus.send_periodic(diag_start2, period=500)
        time.sleep(0.15)
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00)], extended_id=False)
        self.Send_specific_messaje(diag_start2, 0)
        #bus.send_periodic(diag_start2, period=500)
        time.sleep(0.15)
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x22), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00)], extended_id=False)
        self.Send_specific_messaje(diag_start2, 0)
        #bus.send_periodic(diag_start2, period=500)
        time.sleep(0.15)
        #print "hola"
    def run(self):
        global Arrleglo_de_senales
        print(can.detect_available_configs())
        print(can.detect_available_configs(interfaces=['vector']))
        global bus
        print(can.interface.detect_available_configs())

        #nuevo_path = os.path.abspath('Y2018_FNV2_CMDB_v18.06_HS3.dbc')
        #db = cantools.database.load_file(nuevo_path)
            #'C:\Users\lsosa\Documents\Scripts\P702_L1_Testing_Scripts\Test Plan Preparations\Test Plans\TellTales\AirBag\Y2018_FNV2_CMDB_v18.06_HS3.dbc')
        # bus = can.interface.Bus(bustype='vector', interface='vector')
        # bus = can.bus.BusABC.channel_info
        #time.sleep(30)
        global texto_botton_send_signal
        global Array_of_messages
        global texto_botton_send_signal
        global Array_of_messages

        while True:
            try:
                for element in Array_of_messages:
                    # print(element.Message_name)
                    example_message = db.get_message_by_name(element.Message_name)

                    array_values = []
                    array_Names = []
                    cadena_de_texto = ""
                    for signal in element.values_array_Check_box:
                        senal_real = example_message.get_signal_by_name(signal.Signal_name)
                        array_Names.append(signal.Signal_name)
                        array_values.append(signal.Selection_value)

                        #print(senal_real._start)
                        #print(senal_real._length)
                    lista = dict(zip(array_Names, array_values))
                    #print(lista)
                    msg = can.Message(arbitration_id=example_message.frame_id,
                                      data=example_message.encode(lista),
                                      extended_id=False)
                    if texto_botton_send_signal.get() != "Start Sending":
                        if(element.Value_send.get() == 1):
                            if(int(element.Periodo_escrito.get()) < element.Perido_contador):
                                element.Perido_contador = element.Perido_contador + 1
                            else:
                                bus.send(msg)
                                element.Perido_contador = 0

                            #bus.send(msg)
                            # self.Periodo_escrito = StringVar()
                            # self.Perido_contador = 0

                time.sleep(0.001)
            except Exception as ex:
                print (str(ex))
                pass
            time.sleep(0.5)

    def wrapping(self, Message, Signal, Value):
        # global texto_botton_send_signal
        global db
        dicti = []
        #global Arrleglo_de_senales

        global Array_of_messages

        example_message = db.get_message_by_name(Message)
        for element in Array_of_messages:
            #print(element.Message_name)
            example_message = db.get_message_by_name(element.Message_name)
            for signal in element.values_array_Check_box:
                #print(signal.Signal_name + ": " + str(signal.array_index))
                senal_real = example_message.get_signal_by_name(signal.Signal_name)
                print(senal_real)
                print(senal_real._start)
                print(senal_real._length)


        lista = dict(zip(db.get_message_by_name(Message).signal_tree, dicti))
        msg = can.Message(arbitration_id=db.get_message_by_name(Message).frame_id, data=example_message.encode(lista),
                          extended_id=False)
        # print Message + " " + Signal + " " + str(Value)
        # print msg
        return msg
    def Send_specific_messaje(self, mensaje, flag):
        try:
            if(flag == 0):
                bus.send(mensaje)
            else:
                pass
                #bus.send_periodic(mensaje, period=100)
            #print("Message sent on {}".format(bus.channel_info))
        except can.CanError:
            pass
            ##print("Message NOT sent")


def DE_List():
    lista_dexx=['did_DE00',
    'did_DE01',
    'did_DE02',
    'did_DE03',
    'did_DE04',
    'did_DE05',
    'did_DE06',
    'did_DE07',
    'did_DE08',
    'did_DE09']
    # with open('DS-ML3T-1A292-CC001(1).mdx', 'w', encoding='utf-8') as xml_file:
    #     treee = xml.etree.ElementTree.parse(xml_file)
        #treee = etree.parse(xml_file)
        #print(r['body'], file=f)
    #with open('DS-ML3T-1A292-CC001(1).mdx', 'rb') as file_ment:
    # with io.open('DS-ML3T-1A292-CC001(1).mdx', 'r', encoding='utf-8') as xml_file:
    #     #print "Hola"
    #     treee = xml.etree.ElementTree.parse(xml_file)
    treee = xml.etree.ElementTree.parse('DS-ML3T-1A292-CC001(1).mdx')

    root = treee.getroot()
    countries = treee.findall("ECU_DATA")
    #print countries
    for child in root.iter('DID'):

        #print child.get('ID')
        if (child.get('ID') in lista_dexx):
            try:
                Nuevo_de = DEXX()
                Nuevo_de.DE = child.get('ID')
                all_descendants = list(child.iter())
                lista_de_nombres = []

                lista_decripts = []
                lista_de_seleccionados = []
                for i in all_descendants:

                    for j in i.iter('SUB_FIELD'):
                        #print j.get('ID') # imprime subfields del DExx
                        #print j.attrib
                        #print j.find('NAME').text #Nombre del vop
                        contador_De_enum_values = 0
                        lista_de_nombres.append(j.find('NAME').text)
                        lista_de_arreglo = []
                        lista_de_Numeros_vops = []
                        descrip = descripciones()
                        for k in j.iter('DATA_DEFINITION'):
                            for m in k.iter('ENUMERATED_PARAMETERS'):

                                for n in m.iter('ENUM_MEMBER'):
                                    #print n.find('DESCRIPTION').text #imprime descripcines de los valores dentro del vop para los select boxes
                                    #lista_de_nombres.append(n.find('DESCRIPTION').text)
                                    try:
                                        lista_de_arreglo.append(n.find('DESCRIPTION').text)
                                        lista_de_Numeros_vops.append(n.find('ENUM_VALUE').text)
                                        contador_De_enum_values = contador_De_enum_values + 1
                                        #if(contador_De_enum_values > 4):
                                            #print "valor con mas de 3 valores" + j.find('NAME').text
                                    except:
                                        pass
                        descrip.array_descriptor = lista_de_arreglo
                        descrip.Valores_numericos = lista_de_Numeros_vops
                        #print lista_de_arreglo
                        lista_decripts.append(descrip)
                        lista_de_seleccionados.append('0x00')
            except:
                pass

            #descrip.array_descriptor = lista_de_arreglo
            #Nuevo_de.Array_descripciones = descrip
            Nuevo_de.Array_descripciones = lista_decripts  # lista_de_arreglo
            Nuevo_de.Arreglo_valores = lista_de_nombres
            Nuevo_de.arreglo_seleccionados = lista_de_seleccionados
            Lista_DEXX.append(Nuevo_de)
class DEXX:
    def __init__(self):
        self.DE = ""
        self.Arreglo_valores = []
        self.Array_descripciones = []
        self.Trama_de_mensaje_De_can = ""
        self.arreglo_seleccionados = []

class combo_object:
    def __init__(self):
        self.Combobox = ttk.Combobox(frame)
        self.identificador = ""

class descripciones:
    def __init__(self):
        self.array_descriptor = []
        self.Valores_numericos = []
def Hola_mundo():
    global Lista_DEXX
    for i in Lista_DEXX:
        print(i.DE)
    #print "Hola"
def First_combo_box_selection(event, arg, arg2, big_list, Lista_de, elemento_de_lista, Super_texto):
    #print big_list[arg.current()]
    global lista_de_entrys
    # print(Lista_de.DE)
    # print arg2[arg.current()]
    # print Super_texto
    global vops_name_context
    # print vops_name_context
    global vops

    vops[Super_texto].value = int(arg2[arg.current()], 16)
    if(Lista_de.DE in "did_DE00"):
        print(vops.did_DE00.data)
    contador = 0
    # for i in lista_de_entrys:
    #     #i.set(vops.did_DE00.data[contador])
    #     gran_texto = str(hex(vops.did_DE00.data[contador])).replace("0x", "")
    #     #i.delete(0, 'end')
    #     if(vops_name_context == "did_DE00"):
    #         i.insert(0,str(hex(vops.did_DE00.data[contador])).replace("0x", ""))
    #     elif (vops_name_context == "did_DE01"):
    #         i.insert(0, str(hex(vops.did_DE01.data[contador])).replace("0x", ""))
    #     i.delete(0, 1)
    #     contador = contador + 1



    Lista_de.arreglo_seleccionados[elemento_de_lista] = arg2[arg.current()]
    arreglo = []
    cadena_texto = ""
    #print Lista_de.arreglo_seleccionados

def tex_input_Motiv(pop, sv, arrelgo_combo):
    global vops
    global vops_name_context
    #print vops_name_context
    global bus
    global vops
    global lista_de_entrys
    #print sv.get()
    global arreglo_sombo_boxes
    #print arreglo_sombo_boxes
    #print arrelgo_combo
    arreglo_temporal_valores_entry = []
    for i_obj in lista_de_entrys:
        texto_esp = ""
        if(i_obj.get() != ""):
            texto_esp = "0x" + str(i_obj.get())
        else:
            texto_esp = "0x00"
        #print texto_esp
        arreglo_temporal_valores_entry.append(int(texto_esp, 16))
        #print i.identificador

    if(vops_name_context == "did_DE00"):
        vops.did_DE00.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE01"):
        vops.did_DE01.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE02"):
        vops.did_DE02.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE03"):
        vops.did_DE03.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE04"):
        vops.did_DE04.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE05"):
        vops.did_DE05.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE06"):
        vops.did_DE06.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE07"):
        vops.did_DE07.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE08"):
        vops.did_DE08.data = arreglo_temporal_valores_entry
    elif (vops_name_context == "did_DE09"):
        vops.did_DE09.data = arreglo_temporal_valores_entry

    ## arreglar comboboxes
    for i in arreglo_sombo_boxes:
        try:
            i.Combobox.current(vops[i.identificador].value)
        except:
            pass

def distinct_and_order(seq): # Order preserving
  ''' Modified version of Dave Kirby solution '''
  seen = set()
  return [x for x in seq if x not in seen and not seen.add(x)]

def Add_signal_to_menu(argumento, Argumento_exto):
    global arreglo_sombo_boxes
    arreglo_sombo_boxes = []
    global list_de_botones
    global vops_name_context
    global lista_de_entrys
    global Label_config_return
    global Label_config_return2
    #print vops_name_context
    for i in list_de_botones:
        #print i['text']
        if i['text'] in Argumento_exto:
            i['bg'] = 'green'
        else:
            i['bg'] = 'grey'
    try:
        for widget in frame.grid_slaves():
            #print widget
            widget.destroy()
        global row_lef_side
        #print (str(argumento))
        global Lista_DEXX
        elem_clicked = Lista_DEXX[argumento]
        vops_name_context = Lista_DEXX[argumento].DE
        #print Lista_DEXX[argumento]
        contador = 0
        #print elem_clicked.Array_descripciones
        #print elem_clicked.Array_descripciones.array_descriptor
        # for j in elem_clicked.Array_descripciones:
        #      print j.array_descriptor
        lista_de_entrys = []
        arreglo_temporal_combo_boxes = []
        arreglo_de_valores_distinct = distinct_and_order(elem_clicked.Arreglo_valores)#list(set(elem_clicked.Arreglo_valores))
        for i in arreglo_de_valores_distinct:
            texto = Label(frame, text=i)#Text(ctr_mid)
            #print elem_clicked.Array_descripciones[contador].array_descriptor
            #print elem_clicked.Array_descripciones#[contador].array_descriptor
            first_combo_box = ttk.Combobox(frame, width=25, values=(elem_clicked.Array_descripciones[contador].array_descriptor))
            first_combo_box.grid(row=contador, column=1)
            try:
                first_combo_box.current(vops[i].value)
            except:
                pass
                #first_combo_box.current(0)
            first_combo_box.bind("<<ComboboxSelected>>",
                                 lambda event,
                                        arg=first_combo_box,
                                        arg2=elem_clicked.Array_descripciones[contador].Valores_numericos,
                                        big_list=elem_clicked.Array_descripciones[contador].array_descriptor,
                                        Lista_de=elem_clicked,
                                        elemento_de_lista = contador,
                                        Super_texto = i:
                                        First_combo_box_selection(event, arg, arg2,big_list, Lista_de, elemento_de_lista, Super_texto))
            obj_meter = combo_object()
            obj_meter.Combobox =first_combo_box
            obj_meter.identificador = i
            arreglo_temporal_combo_boxes.append(obj_meter)
            #arreglo_temporal_combo_boxes.append(obj_meter)
            #texto.insert(INSERT, i)
            texto.grid(row=contador, column=0)

            contador = contador + 1
        """ Agrega Entrys """
        print(arreglo_temporal_combo_boxes)
        arreglo_sombo_boxes = arreglo_temporal_combo_boxes
        if (True):
            texto_temp = Label(frame, text="Raw Input: ")  # Text(ctr_mid)
            texto_temp.grid(row=0, column=2)
            sv1 = StringVar()
            sv1.trace("w", lambda pop, sv=sv1, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text = Entry(frame, width=5, textvariable=sv1)
            nuevo_text.grid(row=0, column=3)
            lista_de_entrys.append(nuevo_text)

            sv2 = StringVar()
            sv2.trace("w", lambda pop, sv=sv2, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text2 = Entry(frame, width=5, textvariable=sv2)
            #nuevo_text2 = Entry(frame, width=5)
            nuevo_text2.grid(row=0, column=4)
            lista_de_entrys.append(nuevo_text2)

            sv3 = StringVar()
            sv3.trace("w", lambda pop, sv=sv3, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text3 = Entry(frame, width=5, textvariable=sv3)
            #nuevo_text3 = Entry(frame, width=5)
            nuevo_text3.grid(row=0, column=5)
            lista_de_entrys.append(nuevo_text3)

            sv4 = StringVar()
            sv4.trace("w", lambda pop, sv=sv4, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text4 = Entry(frame, width=5, textvariable=sv4)
            #nuevo_text4 = Entry(frame, width=5)
            nuevo_text4.grid(row=0, column=6)
            lista_de_entrys.append(nuevo_text4)

            sv5 = StringVar()
            sv5.trace("w", lambda pop, sv=sv5, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text5 = Entry(frame, width=5, textvariable=sv5)
            #nuevo_text5 = Entry(frame, width=5)
            nuevo_text5.grid(row=0, column=7)
            lista_de_entrys.append(nuevo_text5)

            sv6 = StringVar()
            sv6.trace("w", lambda pop, sv=sv6, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text6 = Entry(frame, width=5, textvariable=sv6)
            #nuevo_text6 = Entry(frame, width=5)
            nuevo_text6.grid(row=0, column=8)
            lista_de_entrys.append(nuevo_text6)

            sv7 = StringVar()
            sv7.trace("w", lambda pop, sv=sv7, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text7 = Entry(frame, width=5, textvariable=sv7)
            #nuevo_text7 = Entry(frame, width=5)
            nuevo_text7.grid(row=0, column=9)
            lista_de_entrys.append(nuevo_text7)

            sv8 = StringVar()
            sv8.trace("w", lambda pop, sv=sv8, arreglo_combo=arreglo_sombo_boxes:
                                                                  tex_input_Motiv(pop, sv, arreglo_combo))
            nuevo_text8 = Entry(frame, width=5, textvariable=sv8)
            #nuevo_text8 = Entry(frame, width=5)
            nuevo_text8.grid(row=0, column=10)
            lista_de_entrys.append(nuevo_text8)

            Label_config_return_etiqueta = Label(frame, text="Raw Config: ")
            Label_config_return_etiqueta.grid(row=1, column=2)

            Label_config_return = Label(frame, text="")
            Label_config_return.grid(row=1, column=3)

            Label_config_return2 = Label(frame, text="")
            Label_config_return2.grid(row=1, column=4)

            if vops_name_context == "did_DE07":
                sv9 = StringVar()
                sv9.trace("w", lambda pop, sv=sv9, arreglo_combo=arreglo_sombo_boxes:
                tex_input_Motiv(pop, sv, arreglo_combo))
                nuevo_text9 = Entry(frame, width=5, textvariable=sv9)
                # nuevo_text8 = Entry(frame, width=5)
                nuevo_text9.grid(row=0, column=11)
                lista_de_entrys.append(nuevo_text9)

                sv10 = StringVar()
                sv10.trace("w", lambda pop, sv=sv10, arreglo_combo=arreglo_sombo_boxes:
                tex_input_Motiv(pop, sv, arreglo_combo))
                nuevo_text10 = Entry(frame, width=5, textvariable=sv10)
                # nuevo_text8 = Entry(frame, width=5)
                nuevo_text10.grid(row=0, column=12)
                lista_de_entrys.append(nuevo_text10)



            # print i

    except:
        pass

    # boton_temp = Button(ctr_mid, text='Add Signal', command=Hola_mundo)
    # boton_temp.grid(row=row_lef_side, column=0)
    # row_lef_side = row_lef_side + 1

def Send_Vop():
    global vops_name_context
    print(vops_name_context)
    global bus
    global vops
    global lista_de_entrys
    #arreglo_temporal_valores_entry = []
    arreglo_temporal_valores_entry = vops.did_DE00.data
    # for i in lista_de_entrys:
    #     #print i.get()
    #     arreglo_temporal_valores_entry.append(int(str("0x" + i.get()), 16))


    if(vops_name_context == "did_DE00"):
        arreglo_temporal_valores_entry = vops.did_DE00.data
        temp_array = vops.did_DE00.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x00), temp_array[0], temp_array[1],
                                        temp_array[2]], extended_id=False)
        #self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE00.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE01":
        arreglo_temporal_valores_entry = vops.did_DE01.data
        temp_array = vops.did_DE01.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x01), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE01.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE02":
        arreglo_temporal_valores_entry = vops.did_DE02.data
        temp_array = vops.did_DE02.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x02), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE02.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE03":
        arreglo_temporal_valores_entry = vops.did_DE03.data
        temp_array = vops.did_DE03.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x03), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE03.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE04":
        arreglo_temporal_valores_entry = vops.did_DE04.data
        temp_array = vops.did_DE04.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x04), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE04.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE05":
        arreglo_temporal_valores_entry = vops.did_DE05.data
        temp_array = vops.did_DE05.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x05), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE05.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE06":
        arreglo_temporal_valores_entry = vops.did_DE06.data
        temp_array = vops.did_DE06.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x06), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE06.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE07":
        arreglo_temporal_valores_entry = vops.did_DE07.data
        temp_array = vops.did_DE07.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x07), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], temp_array[8], temp_array[9]], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE07.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE08":
        arreglo_temporal_valores_entry = vops.did_DE08.data
        temp_array = vops.did_DE08.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x08), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE08.data = arreglo_temporal_valores_entry
    elif vops_name_context == "did_DE09":
        arreglo_temporal_valores_entry = vops.did_DE09.data
        temp_array = vops.did_DE09.data
        diag_start2 = can.Message(arbitration_id=1824,
                                  data=[int(0x10), int(0x0B), int(0x2E), int(0xDE), int(0x09), temp_array[0],
                                        temp_array[1],
                                        temp_array[2]], extended_id=False)
        # self.Send_specific_messaje(diag_start2, 0)
        bus.send(diag_start2)
        time.sleep(0.1)
        diag_start3 = can.Message(arbitration_id=1824,
                                  data=[int(0x21), temp_array[3], temp_array[4], temp_array[5], temp_array[6],
                                        temp_array[7], 0, 0], extended_id=False)
        bus.send(diag_start3)
        vops.did_DE09.data = arreglo_temporal_valores_entry



def Get_Vop():
    global vops_name_context
    print(vops_name_context)
    global bus
    global vops
    global lista_de_entrys
    #if (vops_name_context == "did_DE00"):
    n=2
    cadena_de_texto = vops_name_context.split("_")[1]
    arreglo = [cadena_de_texto[i:i + n] for i in range(0, len(cadena_de_texto), n)]
    print(arreglo)
    diag_start1 = can.Message(arbitration_id=1824,
                              data=[int(0x03), int(0x22), int(0xDE), int(arreglo[1]), int(0x00), int(0x00),
                                    int(0x00), int(0x00)], extended_id=False)
    # self.Send_specific_messaje(diag_start1, 0)
    bus.send(diag_start1)
    time.sleep(0.01)
    diag_start1 = can.Message(arbitration_id=1824,
                              data=[int(0x30), int(0x00), int(0x00), int(0x00), int(0x00), int(0x00),
                                    int(0x00), int(0x00)], extended_id=False)
    # self.Send_specific_messaje(diag_start1, 0)
    bus.send(diag_start1)


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

def myfunction2(event):
    Second_Canvas.configure(scrollregion=canvas.bbox("all"),width=560,height=200)


# create the center widgets
global Path_to_Database
Path_to_Database = ""
def Open_Database():
    global Path_to_Database
    name =filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("CanDB files","*.dbc"),("all files","*.*")))
    global db
    Path_to_Database= name
    db = cantools.database.load_file(name)
    for i in db.messages:
        print(i._name)
    waiter().start()
def NewFile():
    Open_Database()
    global texto_botton_send_signal
    for widget in root.grid_slaves():
        # print widget
        widget.destroy()
    global row_1
    boton1 = Button(root, text='Add Signal', command=Add_signal_to_menu)
    boton1.grid(row=row_1, column=0)
    texto_botton_send_signal.set("Start Sending")
    # boton2 = Button(root, text='Start Sending',
    #                 textvariable=texto_botton_send_signal)  # ,lambda event, apuntador =  command=Add_signal_to_menu)
    # # boton2.config(lambda apuntador=boton2: Cambia_texto_boton_envia_senal(apuntador))
    # # boton2.configure(command=Cambia_texto_boton_envia_senal(boton2))
    # boton2.configure(command
    #                  =lambda boton_apuntador=boton2: Cambia_texto_boton_envia_senal(boton_apuntador))
    # boton2.grid(row=row_1, column=1)

    row_1 = row_1 + 1
    #print
    #"New File!"


def Cambia_texto_boton_envia_senal(boton_apuntador):
    global texto_botton_send_signal
    global Array_of_messages
    # self.Signal_name = ""
    # self.array_index = 0
    # self.is_continous = False
    if texto_botton_send_signal.get() == "Start Sending":
        print("start")
        boton_nuew['bg'] = 'red'
        texto_botton_send_signal.set("Stop Sending")
        # texto_botton_send_signal = "Stop Sending"
    else:
        boton_nuew['bg'] = 'yellow'
        texto_botton_send_signal.set("Start Sending")
        print("stop")


    global Array_of_messages

    # class Current_Message_type:
    #     def __init__(self):
    #         self.Message_name = ""
    #         self.Periodo_escrito = StringVar()
    #         self.Perido_contador = 0
    #         self.Value_send = IntVar()
    #         self.values_array_Check_box = []
    #         self.byte_array = []
    #         self.Index_of_array = 0
    #         self.generic_signal_info = []
    #
    # class Second_screen_info:
    #     def __init__(self):
    #         self.Signal_name = ""
    #         self.array_index = 0
    #         self.is_continous = False
    #         self._unit = ""
    #         self.Valor_escrito_senal = StringVar()
    #example_message = db.get_message_by_name(Message)


def bitstring_to_bytes(s):
    n = 8
    arrelgo =  [s[i:i+n] for i in range(0, len(s), n)]
    new_arreglo = []
    for i in arrelgo:
        new_arreglo.append(int(i, 2))
    return new_arreglo



def Second_combobox_selection(event, arg_combobox, arg_mensaje, big_list_signals, combobox_valor, new_Info, arg_senal):
    global Array_of_messages
    print(arg_senal +": " + big_list_signals[arg_combobox.current()].Senal + " " + str(big_list_signals[arg_combobox.current()].Valor))
    for mesage in Array_of_messages:
        for signals in mesage.values_array_Check_box:
            if arg_senal == signals.Signal_name:
                print(arg_combobox.current())
                signals.Selection_value = big_list_signals[arg_combobox.current()].Valor
                signals.array_index = arg_combobox.current()
    # Second_Combobox.bind("<<ComboboxSelected>>", lambda event, arg_combobox=Second_Combobox, arg_mensaje=message_name,
    #                                                     big_list_signals=lista_vacia, combobox_valor=0,
    #                                                     new_index=Info: Second_combobox_selection(event, arg_combobox,
    #                                                                                               arg_mensaje,
    #                                                                                               big_list_signals,
    #                                                                                               combobox_valor,
    #                                                                                               new_index))
    # for i in Arrleglo_de_senales:
    #     if (i.Indice == new_index):
    #         i.Message = arg_mensaje
    #
    # senal_seleccionada = big_list_signals[arg_combobox.current()]
    # # print arg_mensaje + " " +senal_seleccionada
    # Signal = db.get_message_by_name(arg_mensaje).get_signal_by_name(senal_seleccionada)
    # # print Signal
    # lista_vacia = []
    #
    # for i in range(0, len(Signal._choices)):
    #     lista_vacia.append(Signal._choices.items()[i][1])
    # combobox_valor.config(values=(lista_vacia))

def callback_entry(sv, minimun,maximun, Obj_senal, entry):
    try:
        try:
            number = float(entry.get())
            entry.config({"foreground": "White"})
            if (number < minimun):
                Obj_senal.Selection_value = minimun
                entry.config({"background": "Orange"})
            elif ( number > maximun):
                Obj_senal.Selection_value = maximun
                entry.config({"background": "Orange"})
            else:
                Obj_senal.Selection_value = number
                entry.config({"background": "Green"})
        except:
            Obj_senal.Selection_value = minimun
            entry.config({"background": "Red"})
            pass
    except Exception as ex:
        print(ex)

class Senal_valor:
    def __init__(self):
        self.Senal =""
        self.Valor = 0

def Combobox_message_selection(event, combobox, lista_de_mensajes, Info):
    # self.Message_name = "             ############
    # self.Periodo_escrito = StringVar() ###########
    # self.Perido_contador = 0
    # self.Value_send = IntVar() ###################
    # self.values_array_Check_box = [] #############
    # self.byte_array = []
    # self.Index_of_array = 0#######################
    global Array_of_messages
    lista_global_de_mensajes = []
    for mensajes in Array_of_messages:
        lista_global_de_mensajes.append(mensajes.Message_name)
    for widget in frame.grid_slaves():
        # print widget
        widget.destroy()
    Info.List_of_Messages_index = combobox.current()
    message_name = lista_de_mensajes[combobox.current()]
    Info.Message_name =message_name
    print(lista_de_mensajes[combobox.current()])
    example_message = db.get_message_by_name(message_name)
    #print(example_message)
    nwe_list_of_generic_signals = []
    if not message_name in lista_global_de_mensajes:
        contador = 0
        List_to_be_appended_signals = []
        for signal in example_message.signals:
            nwe_list_of_generic_signals.append(signal)
            texto = Label(frame, text=signal._name+ " " )
            texto.grid(row=contador, column=0)
            My_new_signal = Second_screen_info()
            # self.Signal_name = ""
            # self.array_index = 0
            # self.is_continous = False

            My_new_signal.Signal_name = signal._name

            #print(signal._choices.items())
            # for i in range(0, len(signal._choices)):
            #     lista_vacia.append(signal._choices.items()[i][1])
            if signal._unit == "SED":
                My_new_signal._unit = "SED"
                My_new_signal.is_continous = False
                lista_vacia = []
                lista_texto = []
                for i in signal._choices.items():
                    nuevo_objeto = Senal_valor()
                    nuevo_objeto.Senal = list(i)[1]
                    nuevo_objeto.Valor = list(i)[0]
                    lista_texto.append(list(i)[1])
                    lista_vacia.append(nuevo_objeto)
                    #lista_vacia.append(signal._choices.items()[i][1])
                Second_Combobox = ttk.Combobox(frame, width=25, values=sorted(lista_texto))
                Second_Combobox.grid(row=contador, column=1)
                Second_Combobox.current(0)
                Second_Combobox.bind("<<ComboboxSelected>>", lambda event, arg_combobox=Second_Combobox, arg_mensaje=message_name,
                                                         big_list_signals=sorted(lista_vacia, key=lambda x: x.Senal, reverse=False), combobox_valor=0,
                                                         new_Info=Info, arg_senal=signal._name: Second_combobox_selection(event, arg_combobox,
                                                                                                     arg_mensaje,
                                                                                                     big_list_signals,
                                                                                                     combobox_valor,
                                                                                                     new_Info,
                                                                                                     arg_senal))

            else:
                real_Signal = db.get_message_by_name(message_name).get_signal_by_name(signal._name)
                entry1 = Entry(frame, width=20, textvariable=My_new_signal.Valor_escrito_senal)

                try:
                    My_new_signal.Valor_escrito_senal.trace("w", lambda name, index, mode, sv=entry1, minimun= signal._minimum, maximun= signal._maximum, Obj_senal=My_new_signal, obj_entry = entry1: callback_entry(sv, minimun, maximun, Obj_senal, obj_entry))
                except Exception as ex:
                    print(str(ex))
                entry1.delete(0, END)
                entry1.insert(0, real_Signal._minimum)
                entry1.grid(row=contador, column=1)
                # self.Valor_escrito_senal = StringVar()
                My_new_signal._unit = ""
                My_new_signal.is_continous = True
            List_to_be_appended_signals.append(My_new_signal)
            Info.values_array_Check_box = List_to_be_appended_signals
            Info.generic_signal_info = nwe_list_of_generic_signals
            contador=contador+1
            print(signal)
    else:
        _index_od_message_in_array =lista_global_de_mensajes.index(message_name)
        message =  Array_of_messages[_index_od_message_in_array]
        contador = 0
        for signal in message.values_array_Check_box:
            # self.Signal_name = ""
            # self.array_index = 0
            texto = Label(frame, text=signal.Signal_name + " ")
            texto.grid(row=contador, column=0)
            #My_new_signal = Second_screen_info()
            # self.Signal_name = ""
            # self.array_index = 0
            # self.is_continous = False

            #My_new_signal.Signal_name = signal.Signal_name

            # print(signal._choices.items())
            # for i in range(0, len(signal._choices)):
            #     lista_vacia.append(signal._choices.items()[i][1])
            lista_texto = []
            if signal._unit == "SED":
                #My_new_signal.is_continous = False
                lista_vacia = []
                real_Signal = db.get_message_by_name(message_name).get_signal_by_name(signal.Signal_name)
                for i in real_Signal._choices.items():
                    nuevo_objeto = Senal_valor()
                    nuevo_objeto.Senal = list(i)[1]
                    nuevo_objeto.Valor = list(i)[0]
                    lista_texto.append(list(i)[1])
                    lista_vacia.append(nuevo_objeto)
                    #lista_vacia.append(list(i)[1])
                    # lista_vacia.append(signal._choices.items()[i][1])
                Second_Combobox = ttk.Combobox(frame, width=25, values=sorted(lista_texto))
                Second_Combobox.grid(row=contador, column=1)
                Second_Combobox.current(signal.array_index)
                Second_Combobox.bind("<<ComboboxSelected>>",
                                     lambda event, arg_combobox=Second_Combobox, arg_mensaje=message_name,
                                            big_list_signals=sorted(lista_vacia, key=lambda x: x.Senal, reverse=False), combobox_valor=0,
                                            new_Info=Info, arg_senal=signal.Signal_name: Second_combobox_selection(event,
                                                                                                             arg_combobox,
                                                                                                             arg_mensaje,
                                                                                                             big_list_signals,
                                                                                                             combobox_valor,
                                                                                                             new_Info,
                                                                                                             arg_senal))

            else:
                real_Signal = db.get_message_by_name(message_name).get_signal_by_name(signal.Signal_name)
                signal.Valor_escrito_senal = StringVar()
                entry1 = Entry(frame, width=20, textvariable=signal.Valor_escrito_senal)
                try:
                    signal.Valor_escrito_senal.trace("w",
                                                            lambda name, index, mode, sv=entry1, minimun=real_Signal._minimum,
                                                                   maximun=real_Signal._maximum, Obj_senal=signal,obj_entry = entry1: callback_entry(sv, minimun,
                                                                                                           maximun,Obj_senal,obj_entry ))
                    entry1.delete(0, END)
                    print(str(signal.Selection_value))
                    entry1.insert(0, str(signal.Selection_value))
                except Exception as Exp:
                    print(str(Exp))
                entry1.grid(row=contador, column=1)
                pass
                #My_new_signal.is_continous = True
            #List_to_be_appended_signals.append(My_new_signal)
            #Info.values_array_Check_box = List_to_be_appended_signals
            contador = contador + 1
            #print(signal)
        pass


global Array_of_messages
Array_of_messages = []


def Add_Can_signal_to_menu():
    global row_1
    global Arrleglo_de_senales
    global ctr_mid
    global Array_of_messages
    Info = Current_Message_type()
    # self.Message_name = ""
    # self.Periodo_escrito = StringVar() ##########3
    # self.Perido_contador = 0
    # self.Value_send = IntVar() ####################
    # self.values_array_Check_box = []
    # self.byte_array = []
    # self.Index_of_array = 0#####################
    # Mensaje_dinamico = Mensaje_a_ser_enviado()
    Info.Index_of_array = row_1
    gran_lista = []
    for i in db.messages:
         gran_lista.append(i._name)
    first_combo_box = ttk.Combobox(second_frame, width=25, values=sorted(gran_lista))
    first_combo_box.grid(row=row_1, column=0)
    texto = Label(second_frame, text="Periodic: ")
    #second_combo_box = ttk.Combobox(second_frame, width=25, values=sorted(gran_lista))
    texto.grid(row=row_1, column=1)
    first_combo_box.current(0)
    first_combo_box.bind("<<ComboboxSelected>>", lambda  event, argument1=first_combo_box, argument2 = sorted(gran_lista), argument3=Info: Combobox_message_selection(event, argument1,argument2, argument3 ))
    entry1 = Entry(second_frame, width=5, textvariable = Info.Periodo_escrito)
    Info.Periodo_escrito.set("100")
    entry1.grid(row=row_1, column=2)
    new_check = Checkbutton(second_frame, text='Enviar?', variable=Info.Value_send)#, variable=Mensaje_dinamico.estado_envio_periodico)
    new_check.grid(row=row_1, column=3)
    Button(second_frame, text="Desplegar", width=10).grid(row=row_1, column=4)
    Array_of_messages.append(Info)
    row_1 = row_1 + 1

    #Arrleglo_de_senales.append(Mensaje_dinamico)
global row_1
global db
row_1 =1
root = Tk()
#DE_List()
root.title('Model Definition')
root.geometry('{}x{}'.format(460, 350))
global texto_botton_send_signal
texto_botton_send_signal = StringVar()
texto_botton_send_signal.set("Start Sending")
# create all of the main containers

center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

menu = Menu(root)
root.config(menu=menu)
##########################################
##          Menu Section
##########################################
filemenu = Menu(menu)


class Current_Message_type_saveMode:
    def __init__(self):
        self.Message_name = ""
        self.Periodo_escrito = ""
        self.Perido_contador = 0
        self.Value_send = 0
        self.values_array_Check_box = []
        self.byte_array = []
        self.Index_of_array = 0
        self.generic_signal_info = []
        self.List_of_Messages_index = 0
    def reprJSON(self):
        return dict(Message_name = self.Message_name,
        Periodo_escrito = self.Periodo_escrito,
        Perido_contador = self.Perido_contador,
        Value_send = self.Value_send,
        values_array_Check_box = self.values_array_Check_box,
        byte_array = self.byte_array,
        Index_of_array = self.Index_of_array,
        generic_signal_info = self.generic_signal_info,
                    List_of_Messages_index = self.List_of_Messages_index)
    def from_json(cls, json_data: dict):
        return cls(**json_data)
class Second_screen_info_saveMode:
    def __init__(self):
        self.Signal_name = ""
        self.array_index = 0
        self.Selection_value = 0
        self.is_continous = False
        self._unit = ""
        self.Valor_escrito_senal = ""
    def reprJSON(self):
        return dict(Signal_name = self.Signal_name,
        array_index = self.array_index,
        Selection_value = self.Selection_value,
        is_continous = self.is_continous,
        _unit = self._unit,
        Valor_escrito_senal = self.Valor_escrito_senal)
    def from_json(cls, json_data: dict):
        return cls(**json_data)
class List_to_be_saved:
    def __init__(self):
        self.Database_path = ""
        self.Save_array= []
    def reprJSON(self):
        return dict(Database_path = self.Database_path, Save_array = self.Save_array)
    def from_json(cls, json_data: dict):
        return cls(**json_data)
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)
def file_save():
    global Array_of_messages
    global Path_to_Database
    f = filedialog.asksaveasfile(mode='w', defaultextension=".ican",filetypes = (("iCan File","*.ican"),("all files","*.*")))
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    nueva_lista = []
    #
    # class Current_Message_type:
    #     def __init__(self):
    #         self.Message_name = ""
    #         self.Periodo_escrito = StringVar()
    #         self.Perido_contador = 0
    #         self.Value_send = IntVar()
    #         self.values_array_Check_box = []
    #         self.byte_array = []
    #         self.Index_of_array = 0
    #         self.generic_signal_info = []
    #
    # class Second_screen_info:
    #     def __init__(self):
    #         self.Signal_name = ""
    #         self.array_index = 0
    #         self.Selection_value = 0
    #         self.is_continous = False
    #         self._unit = ""
    #         self.Valor_escrito_senal = StringVar()

    for element in Array_of_messages:
        Save_message = Current_Message_type_saveMode()
        Save_message.Message_name = element.Message_name
        Save_message.Periodo_escrito = element.Periodo_escrito.get()
        Save_message.Perido_contador = element.Perido_contador
        Save_message.Value_send = element.Value_send.get()
        #Save_message.values_array_Check_box = Save_message.values_array_Check_box
        Save_message.byte_array = element.byte_array
        Save_message.Index_of_array = element.Index_of_array
        #Save_message.generic_signal_info = element.generic_signal_info
        Save_message.List_of_Messages_index = element.List_of_Messages_index
        array_of_new_signals = []
        for signal in element.values_array_Check_box:
            new_signal = Second_screen_info_saveMode()
            new_signal.Signal_name = signal.Signal_name
            new_signal.array_index = signal.array_index
            new_signal.Selection_value = signal.Selection_value
            new_signal.is_continous = signal.is_continous
            new_signal._unit = signal._unit
            new_signal.Valor_escrito_senal = signal.Valor_escrito_senal.get()
            array_of_new_signals.append(new_signal)
        Save_message.values_array_Check_box = array_of_new_signals
        nueva_lista.append(Save_message)
        Data_ment_to_be_saved = List_to_be_saved()
        Data_ment_to_be_saved.Save_array = nueva_lista
        Data_ment_to_be_saved.Database_path = Path_to_Database

    f.write(json.dumps(Data_ment_to_be_saved.reprJSON(), cls=ComplexEncoder))
    f.close() # `()` was missing.
class Generic:
    @classmethod
    def from_dict(cls, dict):
        obj = cls()
        obj.__dict__.update(dict)
        return obj

def OpenFile():
    global Path_to_Database
    global row_1
    global Arrleglo_de_senales
    global ctr_mid
    global Array_of_messages

    #name = askopenfilename()
    name = filedialog.askopenfilename(initialdir="/", title="Select file",
                               filetypes=(("iCan files", "*.iCan"), ("all files", "*.*")))
    lines = open(name, 'r').read()#[line.rstrip('\n') for line in open(name)]

    print(name)
    print(lines)
    decoded_Data = json.loads(lines, object_hook=Generic.from_dict)

    Path_to_Database = decoded_Data.Database_path
    print(decoded_Data)
    #print(decoded_Data.Save_array)
    print(decoded_Data.Save_array[0].Message_name)
    global db
    db = cantools.database.load_file(Path_to_Database)
    for Message in decoded_Data.Save_array:
        Info = Current_Message_type()
        Info.Message_name = Message.Message_name
        Info.Index_of_array = row_1
        gran_lista = []
        for i in db.messages:
            gran_lista.append(i._name)
        first_combo_box = ttk.Combobox(second_frame, width=25, values=sorted(gran_lista))
        first_combo_box.grid(row=row_1, column=0)
        texto = Label(second_frame, text="Periodic: ")
        # second_combo_box = ttk.Combobox(second_frame, width=25, values=sorted(gran_lista))
        texto.grid(row=row_1, column=1)
        first_combo_box.current(Message.List_of_Messages_index)
        first_combo_box.bind("<<ComboboxSelected>>",
                             lambda event, argument1=first_combo_box, argument2=sorted(gran_lista),
                                    argument3=Info: Combobox_message_selection(event, argument1, argument2, argument3))
        entry1 = Entry(second_frame, width=5, textvariable=Info.Periodo_escrito)
        Info.Periodo_escrito.set(Message.Periodo_escrito)
        entry1.grid(row=row_1, column=2)
        new_check = Checkbutton(second_frame, text='Enviar?',
                                variable=Info.Value_send)  # , variable=Mensaje_dinamico.estado_envio_periodico)
        #new_check.set(Message.Value_send)
        new_check.grid(row=row_1, column=3)
        Button(second_frame, text="Desplegar", width=10).grid(row=row_1, column=4)
        List_to_be_appended_signals = []
        for signals in Message.values_array_Check_box:
            My_new_signal = Second_screen_info()
            My_new_signal.Signal_name = signals.Signal_name
            My_new_signal.array_index = signals.array_index
            My_new_signal.Selection_value = signals.Selection_value
            if signals._unit == "SED":
                My_new_signal._unit = "SED"
                My_new_signal.is_continous = False

            else:
                My_new_signal.Valor_escrito_senal = StringVar()
                My_new_signal._unit = ""
                My_new_signal.is_continous = True
                My_new_signal.Selection_value = signals.Selection_value
            List_to_be_appended_signals.append(My_new_signal)
        Info.values_array_Check_box = List_to_be_appended_signals
        Array_of_messages.append(Info)
        row_1 = row_1 + 1


menu.add_cascade(label="File", menu=filemenu)
#filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open Configuration File", command=OpenFile)
filemenu.add_command(label="Load Database", command=Open_Database)
filemenu.add_command(label="Save", command=file_save)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

#########################################
##          Seccion Ending
#########################################

center.grid(row=1, sticky="nsew")
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, width=200, height=190)
global ctr_mid
ctr_mid = Frame(center, bg='grey', width=300, height=190, padx=3, pady=3)
Second_Canvas = Canvas(ctr_left)
second_frame=Frame(Second_Canvas,width=300, height=190, padx=3, pady=3)
myscrollbar_2=Scrollbar(ctr_left,orient="vertical",command=Second_Canvas.yview)
Second_Canvas.configure(yscrollcommand=myscrollbar_2.set)
myscrollbar_2.pack(side="right",fill="y")
Second_Canvas.pack(side="left",fill="both", expand=True)
Second_Canvas.create_window((0,0),window=second_frame,anchor='nw')
second_frame.bind("<Configure>", myfunction2)
###     Scroll Shit
canvas=Canvas(ctr_mid)
frame=Frame(canvas,width=250, height=190, padx=3, pady=3)
myscrollbar=Scrollbar(ctr_mid,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left",fill="both", expand=True)
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>", myfunction)

#ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)
contador_aumentos = 0
list_de_botones =[]
# for i in Lista_DEXX:
#     boton1 = Button(ctr_left, text=i.DE, command=lambda contador_aumentos_1=contador_aumentos, Argumento_exto=i.DE: Add_signal_to_menu(contador_aumentos_1, Argumento_exto))
#     boton1.grid(row=contador_aumentos,column=0)
#     list_de_botones.append(boton1)
#     contador_aumentos = contador_aumentos + 1
######################3
### boton Sending
boton_nuew = Button(second_frame, text='Start Sending', textvariable=texto_botton_send_signal)
contador_aumentos=contador_aumentos+1
boton_nuew.grid(row=0,column=0)
boton_nuew['bg'] = 'yellow'
boton_nuew.configure(command =lambda boton_apuntador=boton_nuew: Cambia_texto_boton_envia_senal(boton_apuntador))

################################

boton_nuew2 = Button(second_frame, text="Add Message", command=Add_Can_signal_to_menu)
contador_aumentos=contador_aumentos+1
boton_nuew2.grid(row=0,column=1)


ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
#ctr_right.grid(row=0, column=2, sticky="ns")
waiter().start()
reader().start()
root.mainloop()