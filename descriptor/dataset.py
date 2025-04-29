import schnetpack as spk
import schnetpack.transform as trn

total_path = './RND/data/total.db'
# Load the dataset
# original training num=575, validdation num=95, total num=670
total_data = spk.data.AtomsDataModule(
    total_path,
    batch_size=10,
    distance_unit='Ang',
    property_units={
        'ref_energy': 'eV',
        'ref_stress': 'GPa',
        'ref_force': 'eV/Angstrom'
    },
    num_train=575,
    num_val=95,
    transforms=[
        trn.ASENeighborList(cutoff=2.8),
#         trn.RemoveOffsets("energy", remove_mean=True, remove_atomrefs=False),
        trn.CastTo32()
    ],
    num_workers=1,
    pin_memory=True, # set to false, when not using a GPU
)
total_data.prepare_data()
total_data.setup()