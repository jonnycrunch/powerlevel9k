#!/usr/bin/env zsh
#vim:ft=zsh ts=2 sw=2 sts=2 et fenc=utf-8

# Required for shunit2 to run correctly
setopt shwordsplit
SHUNIT_PARENT=$0

function setUp() {
  export TERM="xterm-256color"
  # Load Powerlevel9k
  source powerlevel9k.zsh-theme
}

function testCustomDirectOutputSegment() {
    local POWERLEVEL9K_CUSTOM_WORLD="echo world"
    local POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(custom_world)

    assertEquals "%K{white} %F{black}world %k%F{white}%f " "$(build_left_prompt)"
}

function testCustomClosureSegment() {
    local POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(custom_world)
    function p9k_hello_world() {
        echo "world"
    }
    local POWERLEVEL9K_CUSTOM_WORLD='p9k_hello_world'

    assertEquals "%K{white} %F{black}world %k%F{white}%f " "$(build_left_prompt)"
}

function testSettingBackgroundForCustomSegment() {
    local POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(custom_world)
    local POWERLEVEL9K_CUSTOM_WORLD="echo world"
    local POWERLEVEL9K_CUSTOM_WORLD_BACKGROUND="yellow"

    assertEquals "%K{yellow} %F{black}world %k%F{yellow}%f " "$(build_left_prompt)"
}

function testSettingForegroundForCustomSegment() {
    local POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(custom_world)
    local POWERLEVEL9K_CUSTOM_WORLD="echo world"
    local POWERLEVEL9K_CUSTOM_WORLD_FOREGROUND="red"

    assertEquals "%K{white} %F{red}world %k%F{white}%f " "$(build_left_prompt)"
}

function testSettingVisualIdentifierForCustomSegment() {
    local POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(custom_world)
    local POWERLEVEL9K_CUSTOM_WORLD="echo world"
    local POWERLEVEL9K_CUSTOM_WORLD_ICON="hw"

    assertEquals "%K{white} %F{black%}hw %f%F{black}world %k%F{white}%f " "$(build_left_prompt)"
}

function testSettingVisualIdentifierForegroundColorForCustomSegment() {
    local POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(custom_world)
    local POWERLEVEL9K_CUSTOM_WORLD="echo world"
    local POWERLEVEL9K_CUSTOM_WORLD_ICON="hw"
    local POWERLEVEL9K_CUSTOM_WORLD_VISUAL_IDENTIFIER_COLOR="red"

    assertEquals "%K{white} %F{red%}hw %f%F{black}world %k%F{white}%f " "$(build_left_prompt)"
}

source shunit2/source/2.1/src/shunit2