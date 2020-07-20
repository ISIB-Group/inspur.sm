.. ...........................................................................
.. © Copyright Inspur Corporation 2020                                          .
.. ...........................................................................

Quickstart
==========

After you install the collection outlined in the  `installation`_ guide, you
can access the collection and the ansible-doc covered in the following topics:

.. _installation:
   installation.html

sm
------------

After the collection is installed, you can access the collection content for a
playbook by referencing the namespace ``inspur`` and the collection's fully
qualified name ``sm``. For example:

.. code-block:: yaml

  -hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get user information"
    inspur.sm.user_info:
      provider: "{{ ism }}"


In Ansible 2.9, the ``collections`` keyword was added to reduce the need
to refer to the collection repeatedly. For example, you can use the
``collections`` keyword in your playbook:

.. code-block:: yaml

  -hosts: ism
  collections:
    - isnpur.sm
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get user information"
    user_info:
      provider: "{{ ism }}"


ansible-doc
-----------

Modules included in this collection provide additional documentation that is
similar to a UNIX, or UNIX-like operating system man page (manual page). This
documentation can be accessed from the command line by using the
``ansible-doc`` command.

Here's how to use the ``ansible-doc`` command after you install the
**Inspur sm collection**: ``ansible-doc inspur.sm.user_info``

.. code-block:: sh

	> USER_INFO    (/root/.ansible/collections/ansible_collections/inspur/sm/plugins/modules/user_info.py)

			Get user information on Inspur server.

	  * This module is maintained by The Ansible Community
	OPTIONS (= is mandatory):

	- host
			Specifies the DNS host name or address for connecting to the remote device over the specified transport.  The value of host
			is used as the destination address for the transport.
			[Default: (null)]
			type: str

	- password
			Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task,
			the value of environment variable `ANSIBLE_NET_PASSWORD' will be used instead.
			[Default: (null)]
			type: str

	- provider
			A dict object containing connection details.
			[Default: (null)]
			suboptions:
			  host:
				description:
				- Specifies the DNS host name or address for connecting to the remote device over
				  the specified transport.  The value of host is used as the destination address
				  for the transport.
				type: str
			  password:
				description:
				- Specifies the password to use to authenticate the connection to the remote device.
				  If the value is not specified in the task, the value of environment variable
				  `ANSIBLE_NET_PASSWORD' will be used instead.
				type: str
			  username:
				description:
				- Configures the username to use to authenticate the connection to the remote
				  device. If the value is not specified in the task, the value of environment
				  variable `ANSIBLE_NET_USERNAME' will be used instead.
				type: str
			
			type: dict

	- username
			Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the
			task, the value of environment variable `ANSIBLE_NET_USERNAME' will be used instead.
			[Default: (null)]
			type: str


	AUTHOR: WangBaoshan (@ISIB-group)
			METADATA:
			  status:
			  - preview
			  supported_by: community
			

	EXAMPLES:

	- name: User test
	  hosts: ism
	  connection: local
	  gather_facts: no
	  vars:
		ism:
		  host: "{{ ansible_ssh_host }}"
		  username: "{{ username }}"
		  password: "{{ password }}"

	  tasks:

	  - name: "Get user information"
		user_info:
		  provider: "{{ ism }}"


	RETURN VALUES:

	message:
		description: Messages returned after module execution.
		returned: always
		type: str
	state:
		description: Status after module execution.
		returned: always
		type: str
	changed:
		description: Check to see if a change was made on the device.
		returned: always
		type: bool


For more information on using the ``ansible-doc`` command, refer
to `Ansible guide`_.

.. _Ansible guide:
   https://docs.ansible.com/ansible/latest/cli/ansible-doc.html#ansible-doc



