.. include:: global.rst.inc
.. highlight:: bash
.. _installation:

Installation
============

.. raw:: html

    <script src="https://asciinema.org/a/0lglEIPiYhsceMExzOKHBUcdZ.js" id="asciicast-0lglEIPiYhsceMExzOKHBUcdZ" async data-speed="1" data-theme="tango"></script>

More Screencasts: `Basic setup`_, `Atlantis setup`_, `Atlantis provision`_, `Project provision`_

Prerequisites
~~~~~~~~~~~~~


The preferred method to install |project_name| is ``pip``; to install it you must do:

On MacOS (depends on `Brew <https://brew.sh>`__):

::

    brew install python3

Or if you already have python2 installed do:

::

    brew upgrade python


On Linux Systems:

::

    - Ubuntu/Debian:
    sudo apt install python3-pip

    - RedHat/Fedora:
    sudo dnf install python3-pip

After this you will be able to install appflow using:

::

    pip3 install appflow

this will install the appflow executable you will use.

This installation is incomplete without initializing the playbooks and your tenant.
To initialize use:

::

   appflow init

Then follow the simple instructions to choose your tenant name and default environment.

At this point the installation is **complete**. Now we will illustrate the folder structure.


Others
~~~~~~

**Fix Ansible problems on 14.04**

The python3 version Shipped with Ubuntu 14.04 is not enough to use ansible from pip3 that Appflow
brings as dependency.
We need to remove it and default to the PPA installation:

::

    -  sudo pip3 uninstall ansible
    -  sudo apt install python2 python2-pip python3 python3-pip git
    -  sudo apt-add-repository ppa:ansible/ansible
    -  sudo apt install ansible


.. start-badges

.. _Basic setup: https://asciinema.org/a/VRlp5YqiT4gvKXrYFYZW9Oz3l?autoplay=1&speed=1
.. _Atlantis setup: https://asciinema.org/a/pcApeQ82UF7kXrygK5jnv9GBA?autoplay=1&speed=1
.. _Atlantis provision: https://asciinema.org/a/BlCYYwDRMFAg31XrfwAY6Z8yc?autoplay=1&speed=1
.. _Project provision: https://asciinema.org/a/lWERm9quxFM91hBnGDBr1UIgH?autoplay=1&speed=1
