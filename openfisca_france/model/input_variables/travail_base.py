# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from openfisca_core.columns import BoolCol, EnumCol, FixedStrCol, FloatCol, IntCol, reference_input_variable
from openfisca_core.enumerations import Enum

from ...entities import Individus


QUIFOY = Enum(['vous', 'conj', 'pac1', 'pac2', 'pac3', 'pac4', 'pac5', 'pac6', 'pac7', 'pac8', 'pac9'])
QUIFAM = Enum(['chef', 'part', 'enf1', 'enf2', 'enf3', 'enf4', 'enf5', 'enf6', 'enf7', 'enf8', 'enf9'])
QUIMEN = Enum(['pref', 'cref', 'enf1', 'enf2', 'enf3', 'enf4', 'enf5', 'enf6', 'enf7', 'enf8', 'enf9'])


# Socio-economic data
# Données d'entrée de la simulation à fournir à partir d'une enquête ou générées par le générateur de cas type

reference_input_variable(
    column = BoolCol(),
    entity_class = Individus,
    label = u"Entreprise assujettie à la taxe sur les salaires",
    name = 'assujettie_taxe_salaire',
    )
reference_input_variable(
    column = BoolCol(),
    entity_class = Individus,
    label = u"Avantages en nature",
    name = 'avantages_en_nature',
    )
reference_input_variable(
    column = BoolCol(),
    entity_class = Individus,
    label = u"Base pour le calcul du remboursement des frais de transport",
    name = 'base_remboursement_transport',
    )
reference_input_variable(
    column = IntCol(),
    entity_class = Individus,
    label = u"Effectifs de l'entreprise",
    name = 'effectifs_entreprise',
    )
reference_input_variable(
    column = FixedStrCol(max_length = 5),
    entity_class = Individus,
    label = u"Localisation entreprise",
    name = 'localisation_entreprise',  # TODO; à adpater sur le format depcom ?
    )
reference_input_variable(
    column = IntCol(),
    entity_class = Individus,
    label = u"Nombre de tickets restaurant",
    name = 'nombre_tickets_restaurant',
    )
reference_input_variable(
    column = FloatCol(),
    entity_class = Individus,
    label = u"Part d'alternants calculée par rapport avec l'effectif moyen",
    name = 'part_d_alternants',
    )
reference_input_variable(
    column = FloatCol(),
    entity_class = Individus,
    label = u"Indemnités, primes et avantages en argent",
    name = 'primes_salaires',
    )
reference_input_variable(
    column = BoolCol(default = True),
    entity_class = Individus,
    label = u"Entreprise redevable de la taxe d'apprentissage",
    name = 'redevable_taxe_apprentissage',
    )
reference_input_variable(
    column = BoolCol(),
    entity_class = Individus,
    label = u"Salarié au forfait",
    name = 'salarie_au_forfait',
    )
reference_input_variable(
    column = FloatCol(),
    entity_class = Individus,
    label = u"Salaire de base",
    name = 'salaire_base',
    )
reference_input_variable(
    column = FloatCol(default = .5),
    entity_class = Individus,
    label = u"Taux de participation de l'employeur au ticket restaurant",
    name = 'taux_participation_ticket_restaurant',
    )
reference_input_variable(
    column = EnumCol(
        enum = Enum(
            [
                u"prive_non_cadre",
                u"prive_cadre",
                u"public_titulaire_etat",
                u"public_titulaire_militaire",
                u"public_titulaire_territoriale",
                u"public_titulaire_hospitaliere",
                u"public_non_titulaire",
                ],
            ),
        ),
    entity_class = Individus,
    label = u"Catégorie de salarié",
    name = 'type_sal',
    )
reference_input_variable(
    column = FloatCol(),
    entity_class = Individus,
    label = u"Valeur du ticket restaurant",
    name = 'valeur_ticket_restaurant',
    )