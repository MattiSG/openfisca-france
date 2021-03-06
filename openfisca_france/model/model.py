# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014, 2015 OpenFisca Team
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


from .caracteristiques_socio_demographiques import (  # noqa analysis:ignore
    demographie,
    logement,
    )

from . import (  # noqa analysis:ignore
    mesures,
    )

from .prelevements_obligatoires import(  # noqa analysis:ignore
    isf,
    taxe_habitation,
    )

from .prelevements_obligatoires.impot_revenu import (  # noqa analysis:ignore
    charges_deductibles,
    credits_impot,
    ir,
    plus_values_immobilieres,
    reductions_impot,
    variables_reductions_credits,
    )

from .prelevements_obligatoires.prelevements_sociaux.contributions_sociales import (  # noqa analysis:ignore
    activite,
    capital,
    remplacement,
    )

from .prelevements_obligatoires.prelevements_sociaux.cotisations_sociales import (  # noqa analysis:ignore
    allegements,
    # penalites,
    # remuneration_public,
    travail_fonction_publique,
    travail_prive,
    travail_totaux,
    )

from .prelevements_obligatoires.prelevements_sociaux import taxes_salaires_main_oeuvre # noqa analysis:ignore

from .prestations import (  # noqa analysis:ignore
    aides_logement,
    education,
    )

from prestations.minima_sociaux import (  # noqa analysis:ignore
    aah,
    asi_aspa,
    ass,
    cmu,
    rsa,
    )

from prestations.prestations_familiales import (  # noqa analysis:ignore
    aeeh,
    af,
    ars,
    asf,
    paje,
    cf,
    )

from revenus import autres

from revenus.activite import (  # noqa analysis:ignore
    non_salarie,
    salarie,
    )



from revenus.capital import (  # noqa analysis:ignore
    financier,
    foncier,
    plus_value,
    )

from revenus.remplacement import (  # noqa analysis:ignore
    chomage,
    retraite,
    indemnites_journalieres_securite_sociale,
    )

