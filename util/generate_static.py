#!/usr/bin/env python
'''
  given tumour and normal vcf pairs, explore msi status
'''

import argparse
import csv
import gzip
import logging
import sys

# #bin	name	chrom	strand	txStart	txEnd	cdsStart	cdsEnd	exonCount	exonStarts	exonEnds	score	name2	cdsStartStat	cdsEndStat	exonFrames
#0	NM_032291	chr1	+	66999638	67216822	67000041	67208778	25	66999638,67091529,67098752,67101626,67105459,67108492,67109226,67126195,67133212,67136677,67137626,67138963,67142686,67145360,67147551,67154830,67155872,67161116,67184976,67194946,67199430,67205017,67206340,67206954,67208755,	67000051,67091593,67098777,67101698,67105516,67108547,67109402,67126207,67133224,67136702,67137678,67139049,67142779,67145435,67148052,67154958,67155999,67161176,67185088,67195102,67199563,67205220,67206405,67207119,67216822,	0	SGIP1	cmpl	cmpl	0,1,2,0,0,0,1,0,0,0,1,2,1,1,1,1,0,1,1,2,2,0,2,1,1,
def main(tx, ofh):
  logging.info('starting...')
  
  odw = csv.DictWriter(ofh, delimiter='\t', fieldnames=['gene', 'tx', 'chrom', 'txstart', 'txend', 'genome'])
  odw.writeheader()
  for r in csv.DictReader(gzip.open(tx, 'rt'), delimiter='\t'):
    odw.writerow({'gene': r['name2'], 'chrom': r['chrom'], 'tx': r['name'], 'txstart': r['txStart'], 'txend': r['txEnd'], 'genome': 'GRCh37'})

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='data for genome helper')
  parser.add_argument('--tx', required=True, help='tumour vcf')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.tx, sys.stdout)
