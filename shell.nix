let
  nixpkgs = fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/tarball/nixos-25.05";
    sha256 = "062g9k0dn0x6a7pcc4w17gkv7sd8gnbbsbr8cmihqdpsrs355gmp";
  };
  pkgs = import nixpkgs { config = {allowUnfree=true;}; overlays = []; };
in

let
  shell_packages = with pkgs; [
    git
    pre-commit
    uv
    cargo
    rustup
    vscode
    docker
      podman
      jq
  ];
in

pkgs.mkShell {
  buildInputs = shell_packages;

  shellHook = ''
    has_venv_dir=false
    has_pyproject=false
    is_linux=false

    [ -d ".venv" ] && has_venv_dir=true
    [ -f "pyproject.toml" ] && has_pyproject=true
    [ "$(uname -s)" = "Linux" ] && is_linux=true

    if ! $has_venv_dir && $has_pyproject; then
      echo "Creating a virtual environment..."
      uv sync
    fi

    if $has_venv_dir; then
      echo "Activating the virtual environment..."
      source .venv/bin/activate
    fi

    if ! $is_linux; then
      podman_vm_state=$(podman machine info --format json | jq -r '.Host.MachineState')
      podman_vm_running=false
      [ "$podman_vm_state" = "Running" ] && podman_vm_running=true
      if ! $podman_vm_running; then
        echo "Starting the podman VM..."
        podman machine start
      fi
    fi
  '';
}
