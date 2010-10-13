import pexpect


HOST	 = 'username@host-name'
PORT	 = '7070'
PASSWORD = 'password'

child = pexpect.spawn('ssh -qTfnN -D %s %s'%(PORT,HOST))
child.expect('password:')
child.sendline(PASSWORD)
child.expect(pexpect.EOF, timeout=None)