#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of spaintvs.
#
#    spaintvs is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    spaintvs is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with spaintvs.  If not, see <http://www.gnu.org/licenses/>.

# Módulo para descargar todos los vídeos de la web de rtve.es ("A la carta" o no)
# Antes era el módulo de tvalacarta.py modificado para dar soporte a todos los vídeos


__all__ = ["cuatro", "Error", "grupo_a3", "tve"] #Canal, Descargar u Utiles no deberían ser utilizadas fuera del paquete
__version__ = "0.0.1"
__author__ = "aabilio <aabilio@gmail.com>"
__date__ = "$10-oct-2012 11:01:48$"