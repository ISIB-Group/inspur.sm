# inspur sm Collection

This repo contains the `inspur.sm` Ansible Collection. Inspur server supports ansible management device,Basic management of the server based on restful interface.

## Tested with Ansible

Tested with the current Ansible 2.10 releases and the current development version of Ansible. Ansible versions before 2.10.0 are not supported.

## External requirements

Circumstance instruction:
Ansible module is suitable for ansible version 2.10

Main steps:

Install suitable Ansible master
Install inspur_sm_sdk 
<!--- A step-by-step reproduction of the problem is helpful if there is no related issue -->
Thes modules require the following to be installed on the Ansible server:

* Python 3.7 or later
* [Ansible](http://www.ansible.com) 2.10 or later
* [Inspur support] inspur_sm_sdk

## Included content

Please check the included content on the [Ansible Galaxy page for this collection](https://galaxy.ansible.com/inspur/sm)

## Using this collection

Before using the General community collection, you need to install the collection with the `ansible-galaxy` CLI:

    ansible-galaxy collection install inspur.sm

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml` using the format:

```yaml
collections:
- name: inspur.sm
```

See [Ansible Using collections](https://isib-group.github.io/inspur.sm-docs/index.html) for more details.

## Contributing to this collection

If you want to develop new content for this collection or improve what is already here, the easiest way to work on the collection is to clone it into one of the configured [`COLLECTIONS_PATH`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths), and work on it there.

You can find more information in the [developer guide for collections](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#contributing-to-collections), and in the [Ansible inspur.sm Guide](https://isib-group.github.io/inspur.sm-docs/index.html).

### Running tests

See [here](https://docs.ansible.com/ansible/devel/dev_guide/developing_collections.html#testing-collections).

### Communication

wangbaoshan@inspur.com


### Publishing New Version

Basic instructions without release branches:

1. Create `changelogs/fragments/<version>.yml` with `release_summary:` section (which must be a string, not a list).
2. Run `antsibull-changelog release --collection-flatmap yes`
3. Make sure `CHANGELOG.rst` and `changelogs/changelog.yaml` are added to git, and the deleted fragments have been removed.
4. Tag the commit with `<version>`. Push changes and tag to the main repository.

## Release notes

See the [changelog](https://github.com/ISIB-Group/inspur.sm/blob/main/CHANGELOG.rst).

## Roadmap

See [this issue](https://github.com/ISIB-Group/inspur.sm/issues/27) for information on releasing, versioning and deprecation.

In general, we plan to release a major version every year, and minor versions every three months. Major versions can contain breaking changes, while minor versions only contain new features and bugfixes.


## More information

- [Ansible Collection overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community code of conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [COPYING](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.
