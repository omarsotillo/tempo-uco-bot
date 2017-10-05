# -*- coding: utf-8 -*-

# Author: Omar Sotillo Franco
# Twitter:  @imos.io
# Description: Bot for telegram that tells you the arrivals and departs of the
# Campus of Rabanales.

############################################
#                 LIBRARIES                #
############################################

import telebot
from telebot import types
import time
import sys

############################################
#                 PRE-BUILD                #
############################################
import datetime

reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = 'Your token goes here'

bot = telebot.TeleBot(TOKEN)


# Con esto, estamos definiendo una función llamada 'listener', que recibe
# como parámetro un dato llamado 'messages'.
def listener(messages):
    for m in messages:  # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text':
            cid = m.chat.id  # Almacenaremos el ID de la conversación.
        if cid > 0:
            # Si 'cid' es positivo, usaremos 'm.chat.first_name' para el nombre
            print str(m.chat.first_name) + " [" + str(cid) + "]: " + m.text
        else:
            # Si 'cid' es negativo, usaremos 'm.from_user.first_name' para el
            # nombre
            print str(m.from_user.first_name) + "[" + str(cid) + "]: " + m.text

# Así, le decimos al bot que utilice como función escuchadora nuestra
# función 'listener' declarada arriba.
bot.set_update_listener(listener)


############################################
#                 KEYBOARD                  #
############################################
keyboard_base = types.ReplyKeyboardMarkup()
keyboard_base.add('🚌 Autobuses', '🚉 Trenes')
keyboard_base.add('🔧 Más')
keyboard_base.resize_keyboard = True

keyboard_bus = types.ReplyKeyboardMarkup()
keyboard_bus.add('📗 Rabanales', '🏡 Colón')
keyboard_bus.add('🔙 Volver')
keyboard_bus.resize_keyboard = True

keyboard_tren = types.ReplyKeyboardMarkup()
keyboard_tren.add('📚 Rabanales', '🚞 Renfe')
keyboard_tren.add('🔙 Volver')
keyboard_tren.resize_keyboard = True

keyboard_more = types.ReplyKeyboardMarkup()
keyboard_more.add('🕑 Horarios Completos', '📅 Disponibilidad')
keyboard_more.add('💡 Créditos', '🔙 Volver')
keyboard_more.resize_keyboard = True


############################################
#                 getTime                    #
############################################
def getTime():
    string_hour = str(int(datetime.datetime.now().hour) + 2)
    string_minute = str(datetime.datetime.now().minute)

    if len(string_hour) == 1:
        string_hour = "0" + string_hour
    if len(string_minute) == 1:
        string_minute = "0" + string_hour

    string_actual = string_hour + ':' + string_minute

    if string_actual >= "22:25":
        string_actual = "00:00"

    return string_actual

Welcome = "🚌 Autobuses : Salidas desde Rabanales y Colón.\n🚉 Trenes : Salidas desde Rabanales y Renfe.\n🕑 Horarios Completos: Foto con horarios completos.\n📅 Disponibilidad : Información sobre servicios.\n💡 Créditos: ¿Quién me ha hecho?\n"

############################################
#                 START                    #
############################################


@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, Welcome, reply_markup=keyboard_base)


@bot.message_handler(func=lambda msg: msg.text == "🔙 Volver")
@bot.message_handler(commands=['volver'])
def command_back_bus(m):
    cid = m.chat.id
    bot.send_message(
        cid, "🚌 Autobuses : Salidas desde Rabanales y Colón.\n🚉 Trenes : Salidas desde Rabanales y Renfe.\n", reply_markup=keyboard_base)

# OKdasda
############################################
#                 AUTOBUSES                #
############################################


@bot.message_handler(func=lambda msg: msg.text == "🚌 Autobuses")
@bot.message_handler(commands=['busmenu'])
def command_menu_bus(m):
    cid = m.chat.id

    bot.send_message(
        cid, "📗 Rabanales: Próxima salida desde Rabanales.\n🏡 Colón: Próxima salida desde Colon", reply_markup=keyboard_bus)


@bot.message_handler(func=lambda msg: msg.text == "📗 Rabanales")
@bot.message_handler(commands=['busrabanales'])
def command_bus_rabanales(m):
    cid = m.chat.id

    string_actual = getTime()

    horario_bus_rabanales = ["07:15", "07:35", "08:00", "08:30", "09:00", "09:20", "09:30", "10:00", "10:30",
                             "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:35", "14:38", "15:00", "15:25",
                             "15:30", "16:15", "17:00", "17:45", "18:30", "19:15", "19:40", "20:00", "20:15", "21:00", "22:25"]

    for element in horario_bus_rabanales:
        if string_actual < element:
            break

    next_bus = "El próximo autobus sale a las " + element + " desde Rabanales."
    bot.send_message(cid, next_bus, reply_markup=keyboard_base)


@bot.message_handler(func=lambda msg: msg.text == "🏡 Colón")
@bot.message_handler(commands=['buscolon'])
def command_bus_colon(m):
    cid = m.chat.id

    string_actual = getTime()

    horario_bus_colon = ["07:00", "07:10", "07:30", "07:55", "08:00", "08:25", "08:30", "08:50", "09:00",
                         "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:25",
                         "14:35", "15:15", "16:45", "17:30", "18:15", "19:00", "19:45", "20:00", "21:30", "22:50"]

    for element in horario_bus_colon:
        if string_actual < element:
            break

    next_bus = "El próximo autobus sale a las " + element + " desde Colón."
    bot.send_message(cid, next_bus, reply_markup=keyboard_base)


############################################
#                 TRENES                   #
############################################
@bot.message_handler(func=lambda msg: msg.text == "🚉 Trenes")
@bot.message_handler(commands=['trenmenu'])
def command_menu_tren(m):
    cid = m.chat.id

    bot.send_message(
        cid, "📚 Rabanales: Próxima salida desde Rabanales.\n🚞 Renfe: Pŕoxima salida desde Renfe", reply_markup=keyboard_tren)


@bot.message_handler(func=lambda msg: msg.text == "📚 Rabanales")
@bot.message_handler(commands=['trenrabanales'])
def command_tren_rabanales(m):
    cid = m.chat.id

    string_actual = getTime()

    horario_tren_rabanales = ["07:26", "07:51", "08:26", "08:56", "09:31", "10:16", "11:06",
                              "12:11", "13:16", "14:16", "14:41", "15:11", "15:56", "16:56", "17:56", "19:16",
                              "19:46", "20:31", "21:31"]

    for element in horario_tren_rabanales:
        if string_actual < element:
            break

    next_tren = "El próximo tren sale a las " + element + " desde Rabanales."

    bot.send_message(cid, next_tren, reply_markup=keyboard_base)


@bot.message_handler(func=lambda msg: msg.text == "🚞 Renfe")
@bot.message_handler(commands=['trenrenfe'])
def command_tren_renfe(m):
    cid = m.chat.id

    string_actual = getTime()

    horario_tren_renfe = ["07:15", "07:40", "08:15", "08:45", "09:20", "10:05", "10:45",
                          "12:00", "13:05", "14:05", "14:30", "15:00", "15:45", "16:45", "17:45", "19:05",
                          "19:35", "20:20", "21:20"]

    for element in horario_tren_renfe:
        if string_actual < element:
            break

    next_tren = "El próximo tren sale a las " + element + " desde Renfe."

    bot.send_message(cid, next_tren, reply_markup=keyboard_base)


############################################
#                 MORE                     #
############################################
@bot.message_handler(func=lambda msg: msg.text == "🔧 Más")
@bot.message_handler(commands=['masmenu'])
def command_menu_mas(m):
    cid = m.chat.id

    bot.send_message(cid, "🕑 Horarios Completos: Foto con horarios completos.\n📅 Disponibilidad : Información sobre servicios.\n💡 Créditos: ¿Quién me ha hecho?", reply_markup=keyboard_more)


@bot.message_handler(func=lambda msg: msg.text == "💡 Créditos")
@bot.message_handler(commands=['creditos'])
def command_creditos(m):
    cid = m.chat.id
    autor = "Mi dueño es Omar Sotillo Franco.🌚🌚\n\nPuedes encontrar más información sobre mi en:\n Twitter : @imos_io\n Telegram: @imos_io\n Correo : kurodasogo@gmail.com\n\nGracias a Eduardo Roldán por su gran colaboración ;D"
    bot.send_message(cid, autor, reply_markup=keyboard_base)


@bot.message_handler(func=lambda msg: msg.text == "📅 Disponibilidad")
@bot.message_handler(commands=['Disponibilidad'])
def command_disponibilidad(m):
    cid = m.chat.id

    bot.send_message(cid, "Los viernes 2, 9, 16 y 23 de octubre se reduce el servicio de trenes con motivo de paros parciales. \nConsulta los horarios para dichos días", reply_markup=keyboard_base)


@bot.message_handler(func=lambda msg: msg.text == "🕑 Horarios Completos")
@bot.message_handler(commands=['Horarios'])
def command_horarios(m):
    cid = m.chat.id
    photo = open("jose.jpg", 'rb')
    bot.send_photo(cid, photo)
    bot.send_message(cid, "Se implementará mañana :)",
                     reply_markup=keyboard_base)


bot.polling(none_stop=True)
