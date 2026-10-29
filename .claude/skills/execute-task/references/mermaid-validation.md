# Validate Mermaid before showing it

Use this for every Mermaid diagram in a repository file or a chat report: an epic Gantt, a Kanban, a workflow. Use the official [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) to parse and render the exact draft to SVG.

## Tool and setup

The verified invocation is `@mermaid-js/mermaid-cli@11.17.0` through `npm exec`; Node/npm and a Chrome or Chromium browser are required. It runs from npm's cache: do not add a `package.json` to this repository.

If a compatible Chrome or Chromium is already installed, set `PUPPETEER_SKIP_DOWNLOAD=true` and pass a temporary Puppeteer JSON config through `--puppeteerConfigFile` with its `executablePath` (check the path exists on this machine; never hard-code another machine's path). In a container that runs as root, the config also needs `"args": ["--no-sandbox"]`.

## Draft, check, show

1. Write the exact diagram body to a UTF-8 `.mmd` file in a temporary directory outside the repository, without the Markdown fence, with its final labels.
2. Render it to a fresh SVG path, so an old SVG cannot pass for success.
3. Require **exit code 0 and a new, non-empty SVG**. A syntax error means fix the `.mmd` and rerun. An install or browser failure means validation did not run: it is not a pass.
4. Put that exact validated text inside the `mermaid` fence. Any change to it needs another run.
5. If validation cannot run, say why and show a table with the same information instead of an unchecked diagram.

```bash
PUPPETEER_SKIP_DOWNLOAD=true npm exec --yes --package=@mermaid-js/mermaid-cli@11.17.0 -- \
  mmdc --puppeteerConfigFile "<puppeteer.json>" --input "<draft.mmd>" --output "<fresh-output.svg>"
echo "exit=$?"; test -s "<fresh-output.svg>" && echo "svg ok"
```

A successful render validates the syntax, not the meaning: check after rendering that the task states and dates in the diagram match the README table and the task files.
