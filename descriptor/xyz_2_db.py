from ase.io import read
import numpy as np
import schnetpack as spk
train_path = './RND/data/training.xyz'
valid_path = './RND/data/validation.xyz'
test_path = './RND/data/test.xyz'
total_path = './RND/data/total.xyz'

H_config_list = read(total_path, index=':')
property_list = []
for H_config in H_config_list:
    ref_energy = H_config.info['REF_energy']
    ref_stress = H_config.info['REF_stress']
    position = H_config.arrays['positions']
    ref_force = H_config.arrays['REF_forces']
    property_list.append({
        'ref_energy': ref_energy,
        'ref_stress': ref_stress,
        'position': position,
        'ref_force': ref_force
    })

total_data = spk.data.ASEAtomsData.create(
    './RND/data/total.db',
    distance_unit='Angstrom',
    property_unit_dict={
        'ref_energy': 'eV',
        'ref_stress': 'GPa',
        'ref_force': 'eV/Angstrom'
    }
)

total_data.add_systems(property_list=property_list, atoms_list=H_config_list)