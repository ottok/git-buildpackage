# vim: set fileencoding=utf-8 :

"""
Test pristine-tar related methods in

    - L{gbp.deb.DebianPristineTar}

and

    - L{gbp.deb.git.DebianGitRepository}

This testcase creates this reposity:

    - A repository at I{repo_dir} called I{repo}

@undocumented: repo_dir test_data
"""

from . import context

import os

repo_dir = context.new_tmpdir(__name__).join('repo')
test_data = os.path.join(context.projectdir, "tests/test_PristineTar_data")

def test_create():
    """
    Create a repository

    Methods tested:
         - L{gbp.deb.git.DebianGitRepository.create}

    >>> import os, gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository.create(repo_dir)
    """

def test_empty_repo():
    """
    Empty repos have no branch pristine-tar branch

    Methods tested:
         - L{gbp.deb.git.DebianGitRepository.has_pristine_tar_branch}
         - L{gbp.deb.pristinetar.DebianPristineTar.has_commit}

    >>> import gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository(repo_dir)
    >>> repo.has_pristine_tar_branch()
    False
    >>> repo.pristine_tar.has_commit('upstream', '1.0', 'gzip')
    False
    """

def test_commit_dir():
    """
    Empty repos have no branch pristine-tar branch

    Methods tested:
         - L{gbp.git.repository.GitRepository.commit_dir}
         - L{gbp.git.repository.GitRepository.create_branch}

    >>> import gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository(repo_dir)
    >>> commit = repo.commit_dir(test_data, msg="initial commit", branch=None)
    >>> repo.create_branch('upstream')
    """

def test_create_tarball():
    """
    Create a tarball from a git tree

    Methods tested:
         - L{gbp.deb.git.DebianGitRepository.archive}

    >>> import gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository(repo_dir)
    >>> repo.archive('tar', 'upstream/', '../upstream_1.0.orig.tar', 'upstream')
    >>> gbp.command_wrappers.Command('gzip', [ '-n', '%s/../upstream_1.0.orig.tar' % repo_dir])()
    """

def test_pristine_tar_commit():
    """
    Commit the delta to the pristine-tar branch

    Methods tested:
         - L{gbp.deb.pristinetar.DebianPristineTar.commit}

    >>> import gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository(repo_dir)
    >>> repo.pristine_tar.commit('../upstream_1.0.orig.tar.gz', 'upstream')
    """

def test_pristine_has_commit():
    """
    Find delta on the pristine tar branch

    Methods tested:
         - L{gbp.deb.pristinetar.DebianPristineTar.has_commit}
         - L{gbp.pkg.pristinetar.PristineTar.get_commit}

    >>> import gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository(repo_dir)
    >>> repo.pristine_tar.has_commit('upstream', '1.0', 'bzip2')
    False
    >>> repo.pristine_tar.has_commit('upstream', '1.0', 'gzip')
    True
    >>> repo.pristine_tar.has_commit('upstream', '1.0')
    True
    >>> branch = repo.rev_parse('pristine-tar')
    >>> commit = repo.pristine_tar.get_commit('upstream_1.0.orig.tar.gz')
    >>> branch == commit
    True
    """

def test_pristine_tar_checkout():
    """
    Checkout a tarball using pristine-tar

    Methods tested:
         - L{gbp.deb.pristinetar.DebianPristineTar.checkout}

    >>> import gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository(repo_dir)
    >>> repo.pristine_tar.checkout('upstream', '1.0', 'gzip', '..')
    """

def test_pristine_tar_checkout_nonexistent():
    """
    Checkout a tarball that does not exist using pristine-tar

    Methods tested:
         - L{gbp.deb.pristinetar.DebianPristineTar.checkout}

    >>> import gbp.deb.git
    >>> repo = gbp.deb.git.DebianGitRepository(repo_dir)
    >>> repo.pristine_tar.checkout('upstream', '1.1', 'gzip', '..')
    Traceback (most recent call last):
    ...
    CommandExecFailed: Pristine-tar couldn't checkout "upstream_1.1.orig.tar.gz": fatal: Path 'upstream_1.1.orig.tar.gz.delta' does not exist in 'refs/heads/pristine-tar'
    pristine-tar: git show refs/heads/pristine-tar:upstream_1.1.orig.tar.gz.delta failed
    """

def test_teardown():
    """
    Perform the teardown

    >>> context.teardown()
    """

# vim:et:ts=4:sw=4:et:sts=4:ai:set list listchars=tab\:»·,trail\:·:
