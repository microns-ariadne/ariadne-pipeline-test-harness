import luigi
import os
# Module generated by ariadne on 2016-03-03 11:45:05.590300
class autoteststage(luigi.Task):
    A=luigi.Parameter()
    def requires(self):
        return 
    def output(self):
        return
    def run(self):
        os.spawnlp(os.P_WAIT, 'ls', 'ls', '-l', self.A)
        return
    def complete(self):
        return 1