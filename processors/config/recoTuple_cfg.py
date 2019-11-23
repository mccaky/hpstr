import HpstrConf
import sys

# Use the input file to set the output file name
lcio_file = sys.argv[1].strip()
root_file = '%s.root' % lcio_file[:-6]

print 'LCIO file: %s' % lcio_file
print 'Root file: %s' % root_file

p = HpstrConf.Process()

# Library containing processors
p.libraries.append("libprocessors.so")

###############################
#          Processors         #
###############################

header = HpstrConf.Processor('header', 'EventProcessor')
track = HpstrConf.Processor('track', 'TrackingProcessor')
svthits = HpstrConf.Processor('svthits', 'Tracker3DHitProcessor')
rawsvt = HpstrConf.Processor('rawsvt', 'SvtRawDataProcessor')
ecal = HpstrConf.Processor('ecal', 'ECalDataProcessor')
mcpart = HpstrConf.Processor('mcpart', 'MCParticleProcessor')

###############################
#   Processor Configuration   #
###############################
#Event

#Tracks
track.parameters["debug"] = 0 
track.parameters["trkCollLcio"] = 'GBLTracks'
track.parameters["trkCollRoot"] = 'GBLTracks'
track.parameters["kinkRelCollLcio"] = 'GBLKinkDataRelations'
track.parameters["trkRelCollLcio"] = 'TrackDataRelations'
track.parameters["trkhitCollRoot"] = 'RotatedHelicalOnTrackHits'
track.parameters["hitFitsCollLcio"] = 'SVTFittedRawTrackerHits'
track.parameters["rawhitCollRoot"] = 'SVTRawHitsOnTrack'

# Sequence which the processors will run.
p.sequence = [header, track, rawsvt, svthits, ecal, mcpart]

p.input_files=[lcio_file]
p.output_files = [root_file]

#p.max_events = 1000

p.printProcess()
