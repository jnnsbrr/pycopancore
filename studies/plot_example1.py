"""Skript to plot Jobsts prototype model results."""

import numpy as np
from numpy import array, average, mean
from pylab import plot, gca, show, figure, subplots, gca, semilogy, legend, tight_layout, NullLocator
from pickle import load

f, ((ax11, ax12), (ax21, ax22), (ax31, ax32)) = subplots(nrows=3, ncols=2, sharex=True, sharey=False)
lws = 1
al = 0.5

# LEFT: without policy

ax11.title.set_text('without social processes')

traj = load(open("/home/jobst/work/without.pickle","rb"))
worlds = list(traj["World.atmospheric_carbon"].keys())
social_systems = list(traj["SocialSystem.population"].keys())
cells = list(traj["Cell.fossil_carbon"].keys())
individuals = list(traj["Individual.is_environmentally_friendly"].keys())
t = np.array(traj['t'])

print(sum(array(traj["SocialSystem.protected_terrestrial_carbon"][s]) for s in social_systems)
      / sum(array(traj["Cell.terrestrial_carbon"][c]) for c in cells))

# cultural
ax11.plot(t[3:], 100*average([array(traj["Individual.is_environmentally_friendly"][i][3:]*1) for i in individuals], axis=0,
#                        weights=[array(traj["Individual.represented_population"][i][3:]*1) for i in individuals]
                        ),color="green",lw=lws, label="env. friendly individuals")
ax11.plot(t[3:], 100*mean([array(traj["SocialSystem.has_renewable_subsidy"][s][3:]*1) for s in social_systems], axis=0),color="darkorange",lw=lws, label="regions w/ renewable subsidy")
ax11.plot(t[3:], 100*mean([array(traj["SocialSystem.has_emissions_tax"][s][3:]*1) for s in social_systems], axis=0),color="blue",lw=lws, label="regions w/ emissions tax")
ax11.plot(t[3:], 100*mean([array(traj["SocialSystem.has_fossil_ban"][s][3:]*1) for s in social_systems], axis=0),color="gray",lw=lws, label="regions w/ fossil ban")
ax11.set_ylabel('percent')
ax11.set_ylim(-5,105)
ax11.legend(title='CUL: opinions & policies')

# metabolic
for i, s in enumerate(social_systems):
    Es = array(traj["SocialSystem.secondary_energy_flow"][s][3:])
    ax21.plot(t[3:], 100*array(traj["SocialSystem.biomass_input_flow"][s][3:]) * 40e9 / Es, color="green", lw=lws, alpha=al, label=None if i else "biomass")
    ax21.plot(t[3:], 100*array(traj["SocialSystem.fossil_fuel_input_flow"][s][3:]) * 47e9 / Es, color="gray", lw=lws, alpha=al, label=None if i else "fossils")
    ax21.plot(t[3:], 100*array(traj["SocialSystem.renewable_energy_input_flow"][s][3:]) / Es, color="darkorange", lw=lws, alpha=al, label=None if i else "renewables")
#plot(t[3:], 100*average([array(traj["biomass_input_flow"][s][3:]) for s in social_systems], axis=0,
#                        weights=[array(traj["population"][s][3:]) for s in social_systems]) * 40e9 / Es, color="green", lw=3, label="global share of biomass energy")
#plot(t[3:], 100*average([array(traj["fossil_fuel_input_flow"][s][3:]) for s in social_systems], axis=0,
#                        weights=[array(traj["population"][s][3:]) for s in social_systems]) * 47e9 / Es, color="gray", lw=3, label="global share of fossil energy")
#plot(t[3:], 100*average([array(traj["renewable_energy_input_flow"][s][3:]) for s in social_systems], axis=0,
#                        weights=[array(traj["population"][s][3:]) for s in social_systems]) / Es, color="darkorange", lw=3, label="global share of renewables")
ax21.set_ylabel('percent')
ax21.set_ylim(-5,105)
ax21.legend(title='MET: energy shares')

# natural
ax31.plot(t[3:], traj["World.atmospheric_carbon"][worlds[0]][3:], color="cyan", lw=2, label="atmosphere")
ax31.plot(t[3:], traj["World.upper_ocean_carbon"][worlds[0]][3:], color="blue", lw=2, label="upper oceans")
ax31.plot(t[3:], sum(array(traj["Cell.terrestrial_carbon"][c][3:]) for c in cells), color="green", lw=2, label="plants & soils")
ax31.plot(t[3:], sum(array(traj["Cell.fossil_carbon"][c][3:]) for c in cells), color="gray", lw=2, label="fossils")
#for i, s in enumerate(social_systems):
#    plot(t[3:], traj["protected_terrestrial_carbon"][s][3:],color="green",lw=lws, label=None if i else "protected biomass")
ax31.set_ylabel('gigatonnes carbon')
ax31.set_ylim(-100,3100)
ax31.legend(title='ENV: global carbon stocks')

ax31.set_xlabel('year')
ax31.set_xlim(1990,2110)

# RIGHT: with policy

ax12.title.set_text('with social processes')

traj = load(open("/home/jobst/work/with.pickle","rb"))
worlds = list(traj["World.atmospheric_carbon"].keys())
social_systems = list(traj["SocialSystem.population"].keys())
cells = list(traj["Cell.fossil_carbon"].keys())
individuals = list(traj["Individual.is_environmentally_friendly"].keys())
t = np.array(traj['t'])

# cultural
ax12.plot(t[3:], 100*average([array(traj["Individual.is_environmentally_friendly"][i][3:]*1) for i in individuals], axis=0,
                        weights=[array(traj["Individual.represented_population"][i][3:]*1) for i in individuals]
                        ),color="green",lw=lws, label="env. friendly individuals")
ax12.plot(t[3:], 100*mean([array(traj["SocialSystem.has_renewable_subsidy"][s][3:]*1) for s in social_systems], axis=0),color="darkorange",lw=lws, label="regions w/ renewable subsidy")
ax12.plot(t[3:], 100*mean([array(traj["SocialSystem.has_emissions_tax"][s][3:]*1) for s in social_systems], axis=0),color="blue",lw=lws, label="regions w/ emissions tax")
ax12.plot(t[3:], 100*mean([array(traj["SocialSystem.has_fossil_ban"][s][3:]*1) for s in social_systems], axis=0),color="gray",lw=lws, label="regions w/ fossil ban")
ax12.set_ylim(-5,105)
ax12.yaxis.set_major_locator(NullLocator())
#ax12.legend()

# metabolic
for i, s in enumerate(social_systems):
    Es = array(traj["SocialSystem.secondary_energy_flow"][s][3:])
    ax22.plot(t[3:], 100*array(traj["SocialSystem.biomass_input_flow"][s][3:]) * 40e9 / Es, color="green", lw=lws, alpha=al, label=None if i else "biomass")
    ax22.plot(t[3:], 100*array(traj["SocialSystem.fossil_fuel_input_flow"][s][3:]) * 47e9 / Es, color="gray", lw=lws, alpha=al, label=None if i else "fossils")
    ax22.plot(t[3:], 100*array(traj["SocialSystem.renewable_energy_input_flow"][s][3:]) / Es, color="darkorange", lw=lws, alpha=al, label=None if i else "renewables")
#plot(t[3:], 100*average([array(traj["biomass_input_flow"][s][3:]) for s in social_systems], axis=0,
#                        weights=[array(traj["population"][s][3:]) for s in social_systems]) * 40e9 / Es, color="green", lw=3, label="global share of biomass energy")
#plot(t[3:], 100*average([array(traj["fossil_fuel_input_flow"][s][3:]) for s in social_systems], axis=0,
#                        weights=[array(traj["population"][s][3:]) for s in social_systems]) * 47e9 / Es, color="gray", lw=3, label="global share of fossil energy")
#plot(t[3:], 100*average([array(traj["renewable_energy_input_flow"][s][3:]) for s in social_systems], axis=0,
#                        weights=[array(traj["population"][s][3:]) for s in social_systems]) / Es, color="darkorange", lw=3, label="global share of renewables")
ax22.set_ylim(-5,105)
ax22.yaxis.set_major_locator(NullLocator())
#ax22.legend()

# natural
ax32.plot(t[3:], traj["World.atmospheric_carbon"][worlds[0]][3:], color="cyan", lw=2, label="atmosphere")
ax32.plot(t[3:], traj["World.upper_ocean_carbon"][worlds[0]][3:], color="blue", lw=2, label="upper oceans")
ax32.plot(t[3:], sum(array(traj["Cell.terrestrial_carbon"][c][3:]) for c in cells), color="green", lw=2, label="plants & soils")
ax32.plot(t[3:], sum(array(traj["Cell.fossil_carbon"][c][3:]) for c in cells), color="gray", lw=2, label="fossils")
#for i, s in enumerate(social_systems):
#    plot(t[3:], traj["protected_terrestrial_carbon"][s][3:],color="green",lw=lws, label=None if i else "protected biomass")
ax32.yaxis.set_major_locator(NullLocator())
ax32.set_ylim(-100,3100)
#ax32.legend()

ax32.set_xlabel('year')
ax32.set_xlim(1990,2110)

f.subplots_adjust(hspace=0, wspace=0)
show()

# TODO: 
# policy shares, env. friendly shares
# transparancy, means
# wellb. abs., renew., pop. log
# total protected
# horiz.
# save dump with codename,uid as key