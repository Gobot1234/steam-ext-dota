# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_client_match_management.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto

from .base_gcmessages import CMsgClientPingData
from .dota_shared_enums import CDOTAClientHardwareSpecs, DOTABotDifficulty,  DOTALobbyReadyState, MatchType


class EStartFindingMatchResult(betterproto.Enum):
    Invalid = 0
    OK = 1
    AlreadySearching = 2
    FailGeneric = 100
    FailedIgnore = 101
    MatchmakingDisabled = 102
    RegionOffline = 103
    MatchmakingCooldown = 104
    ClientOutOfDate = 105
    CompetitiveNoLowPriority = 106
    CompetitiveNotUnlocked = 107
    GameModeNotUnlocked = 108
    CompetitiveNotEnoughPlayTime = 109
    MissingInitialSkill = 110
    CompetitiveRankSpreadTooLarge = 111
    MemberAlreadyInLobby = 112
    MemberNotVACVerified = 113
    WeekendTourneyBadPartySize = 114
    WeekendTourneyTeamBuyInTooSmall = 115
    WeekendTourneyIndividualBuyInTooLarge = 116
    WeekendTourneyTeamBuyInTooLarge = 117
    MemberMissingEventOwnership = 118
    WeekendTourneyNotUnlocked = 119
    WeekendTourneyRecentParticipation = 120
    MemberMissingAnchoredPhoneNumber = 121
    NotMemberOfClan = 122
    CoachesChallengeBadPartySize = 123
    CoachesChallengeRequirementsNotMet = 124
    InvalidRoleSelections = 125
    PhoneNumberDiscrepancy = 126
    NoQueuePoints = 127
    MemberMissingGauntletFlag = 128
    MemberGauntletTooRecent = 129
    DifficultyNotUnlocked = 130
    CoachesNotAllowedInParty = 131
    MatchmakingBusy = 132


@dataclass
class CMsgStartFindingMatch(betterproto.Message):
    key: str = betterproto.string_field(1)
    matchgroups: int = betterproto.uint32_field(2)
    client_version: int = betterproto.uint32_field(3)
    game_modes: int = betterproto.uint32_field(4)
    bot_difficulty: "DOTABotDifficulty" = betterproto.enum_field(5)
    match_type: "MatchType" = betterproto.enum_field(6)
    matchlanguages: int = betterproto.uint32_field(7)
    team_id: int = betterproto.uint32_field(8)
    game_language_enum: "MatchLanguages" = betterproto.enum_field(10)
    game_language_name: str = betterproto.string_field(11)
    ping_data: "CMsgClientPingData" = betterproto.message_field(12)
    region_select_flags: int = betterproto.uint32_field(13)
    solo_queue: bool = betterproto.bool_field(14)
    bot_script_index: int = betterproto.uint32_field(15)
    steam_clan_account_id: int = betterproto.uint32_field(16)
    is_challenge_match: bool = betterproto.bool_field(17)
    lane_selection_flags: int = betterproto.uint32_field(18)
    high_priority_disabled: bool = betterproto.bool_field(19)
    disable_experimental_gameplay: bool = betterproto.bool_field(20)
    custom_game_difficulty_mask: int = betterproto.uint32_field(21)


@dataclass
class CMsgStartFindingMatchResult(betterproto.Message):
    legacy_generic_eresult: int = betterproto.uint32_field(1)
    result: "EStartFindingMatchResult" = betterproto.enum_field(2)
    error_token: str = betterproto.string_field(3)
    debug_message: str = betterproto.string_field(4)
    responsible_party_members: List[float] = betterproto.fixed64_field(5)
    result_metadata: int = betterproto.uint32_field(6)


@dataclass
class CMsgStopFindingMatch(betterproto.Message):
    accept_cooldown: bool = betterproto.bool_field(1)


@dataclass
class CMsgPartyBuilderOptions(betterproto.Message):
    additional_slots: int = betterproto.uint32_field(1)
    match_type: "MatchType" = betterproto.enum_field(2)
    matchgroups: int = betterproto.uint32_field(3)
    client_version: int = betterproto.uint32_field(4)
    language: "MatchLanguages" = betterproto.enum_field(5)


@dataclass
class CMsgReadyUp(betterproto.Message):
    state: "DOTALobbyReadyState" = betterproto.enum_field(1)
    ready_up_key: float = betterproto.fixed64_field(2)
    hardware_specs: "CDOTAClientHardwareSpecs" = betterproto.message_field(3)


@dataclass
class CMsgReadyUpStatus(betterproto.Message):
    lobby_id: float = betterproto.fixed64_field(1)
    accepted_ids: List[int] = betterproto.uint32_field(2)
    declined_ids: List[int] = betterproto.uint32_field(3)


@dataclass
class CMsgAbandonCurrentGame(betterproto.Message):
    pass


@dataclass
class CMsgPracticeLobbySetDetails(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    game_name: str = betterproto.string_field(2)
    team_details: List["CLobbyTeamDetails"] = betterproto.message_field(3)
    server_region: int = betterproto.uint32_field(4)
    game_mode: int = betterproto.uint32_field(5)
    cm_pick: "DOTA_CM_PICK" = betterproto.enum_field(6)
    bot_difficulty_radiant: "DOTABotDifficulty" = betterproto.enum_field(9)
    allow_cheats: bool = betterproto.bool_field(10)
    fill_with_bots: bool = betterproto.bool_field(11)
    intro_mode: bool = betterproto.bool_field(12)
    allow_spectating: bool = betterproto.bool_field(13)
    game_version: "DOTAGameVersion" = betterproto.enum_field(14)
    pass_key: str = betterproto.string_field(15)
    leagueid: int = betterproto.uint32_field(16)
    penalty_level_radiant: int = betterproto.uint32_field(17)
    penalty_level_dire: int = betterproto.uint32_field(18)
    load_game_id: int = betterproto.uint32_field(19)
    series_type: int = betterproto.uint32_field(20)
    radiant_series_wins: int = betterproto.uint32_field(21)
    dire_series_wins: int = betterproto.uint32_field(22)
    allchat: bool = betterproto.bool_field(23)
    dota_tv_delay: "LobbyDotaTVDelay" = betterproto.enum_field(24)
    lan: bool = betterproto.bool_field(25)
    custom_game_mode: str = betterproto.string_field(26)
    custom_map_name: str = betterproto.string_field(27)
    custom_difficulty: int = betterproto.uint32_field(28)
    custom_game_id: int = betterproto.uint64_field(29)
    custom_min_players: int = betterproto.uint32_field(30)
    custom_max_players: int = betterproto.uint32_field(31)
    visibility: "DOTALobbyVisibility" = betterproto.enum_field(33)
    custom_game_crc: float = betterproto.fixed64_field(34)
    custom_game_timestamp: float = betterproto.fixed32_field(37)
    previous_match_override: int = betterproto.uint64_field(38)
    pause_setting: "LobbyDotaPauseSetting" = betterproto.enum_field(42)
    bot_difficulty_dire: "DOTABotDifficulty" = betterproto.enum_field(43)
    bot_radiant: int = betterproto.uint64_field(44)
    bot_dire: int = betterproto.uint64_field(45)
    selection_priority_rules: "DOTASelectionPriorityRules" = betterproto.enum_field(46)
    custom_game_penalties: bool = betterproto.bool_field(47)
    lan_host_ping_location: str = betterproto.string_field(48)
    league_node_id: int = betterproto.uint32_field(49)


@dataclass
class CMsgPracticeLobbyCreate(betterproto.Message):
    search_key: str = betterproto.string_field(1)
    pass_key: str = betterproto.string_field(5)
    client_version: int = betterproto.uint32_field(6)
    lobby_details: "CMsgPracticeLobbySetDetails" = betterproto.message_field(7)
    save_game: "CMsgPracticeLobbyCreateSaveGame" = betterproto.message_field(8)


@dataclass
class CMsgPracticeLobbyCreateSaveGame(betterproto.Message):
    data: bytes = betterproto.bytes_field(1)
    version: int = betterproto.int32_field(2)
    steam_id: float = betterproto.fixed64_field(3)
    signature: float = betterproto.fixed64_field(4)


@dataclass
class CMsgPracticeLobbySetTeamSlot(betterproto.Message):
    team: "DOTA_GC_TEAM" = betterproto.enum_field(1)
    slot: int = betterproto.uint32_field(2)
    bot_difficulty: "DOTABotDifficulty" = betterproto.enum_field(3)


@dataclass
class CMsgPracticeLobbySetCoach(betterproto.Message):
    team: "DOTA_GC_TEAM" = betterproto.enum_field(1)


@dataclass
class CMsgPracticeLobbyJoinBroadcastChannel(betterproto.Message):
    channel: int = betterproto.uint32_field(1)
    preferred_description: str = betterproto.string_field(2)
    preferred_country_code: str = betterproto.string_field(3)
    preferred_language_code: str = betterproto.string_field(4)


@dataclass
class CMsgPracticeLobbyCloseBroadcastChannel(betterproto.Message):
    channel: int = betterproto.uint32_field(1)


@dataclass
class CMsgPracticeLobbyToggleBroadcastChannelCameramanStatus(betterproto.Message):
    pass


@dataclass
class CMsgPracticeLobbyKick(betterproto.Message):
    account_id: int = betterproto.uint32_field(3)


@dataclass
class CMsgPracticeLobbyKickFromTeam(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgPracticeLobbyLeave(betterproto.Message):
    pass


@dataclass
class CMsgPracticeLobbyLaunch(betterproto.Message):
    client_version: int = betterproto.uint32_field(5)


@dataclass
class CMsgApplyTeamToPracticeLobby(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)


@dataclass
class CMsgClearPracticeLobbyTeam(betterproto.Message):
    pass


@dataclass
class CMsgPracticeLobbyList(betterproto.Message):
    pass_key: str = betterproto.string_field(2)
    region: int = betterproto.uint32_field(3)
    game_mode: "DOTA_GameMode" = betterproto.enum_field(4)


@dataclass
class CMsgPracticeLobbyListResponseEntry(betterproto.Message):
    id: int = betterproto.uint64_field(1)
    members: List[
        "CMsgPracticeLobbyListResponseEntryCLobbyMember"
    ] = betterproto.message_field(5)
    requires_pass_key: bool = betterproto.bool_field(6)
    leader_account_id: int = betterproto.uint32_field(7)
    name: str = betterproto.string_field(10)
    custom_game_mode: str = betterproto.string_field(11)
    game_mode: "DOTA_GameMode" = betterproto.enum_field(12)
    friend_present: bool = betterproto.bool_field(13)
    players: int = betterproto.uint32_field(14)
    custom_map_name: str = betterproto.string_field(15)
    max_player_count: int = betterproto.uint32_field(16)
    server_region: int = betterproto.uint32_field(17)
    league_id: int = betterproto.uint32_field(19)
    lan_host_ping_location: str = betterproto.string_field(20)


@dataclass
class CMsgPracticeLobbyListResponseEntryCLobbyMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    player_name: str = betterproto.string_field(2)


@dataclass
class CMsgPracticeLobbyListResponse(betterproto.Message):
    lobbies: List["CMsgPracticeLobbyListResponseEntry"] = betterproto.message_field(2)


@dataclass
class CMsgLobbyList(betterproto.Message):
    server_region: int = betterproto.uint32_field(1)
    game_mode: "DOTA_GameMode" = betterproto.enum_field(2)


@dataclass
class CMsgLobbyListResponse(betterproto.Message):
    lobbies: List["CMsgPracticeLobbyListResponseEntry"] = betterproto.message_field(1)


@dataclass
class CMsgPracticeLobbyJoin(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    client_version: int = betterproto.uint32_field(2)
    pass_key: str = betterproto.string_field(3)
    custom_game_crc: float = betterproto.fixed64_field(4)
    custom_game_timestamp: float = betterproto.fixed32_field(5)


@dataclass
class CMsgPracticeLobbyJoinResponse(betterproto.Message):
    result: "DOTAJoinLobbyResult" = betterproto.enum_field(1)


@dataclass
class CMsgFriendPracticeLobbyListRequest(betterproto.Message):
    friends: List[int] = betterproto.uint32_field(1)


@dataclass
class CMsgFriendPracticeLobbyListResponse(betterproto.Message):
    lobbies: List["CMsgPracticeLobbyListResponseEntry"] = betterproto.message_field(1)


@dataclass
class CMsgJoinableCustomGameModesRequest(betterproto.Message):
    server_region: int = betterproto.uint32_field(1)


@dataclass
class CMsgJoinableCustomGameModesResponseEntry(betterproto.Message):
    custom_game_id: int = betterproto.uint64_field(1)
    lobby_count: int = betterproto.uint32_field(2)
    player_count: int = betterproto.uint32_field(3)


@dataclass
class CMsgJoinableCustomGameModesResponse(betterproto.Message):
    game_modes: List[
        "CMsgJoinableCustomGameModesResponseEntry"
    ] = betterproto.message_field(1)


@dataclass
class CMsgJoinableCustomLobbiesRequest(betterproto.Message):
    server_region: int = betterproto.uint32_field(1)
    custom_game_id: int = betterproto.uint64_field(2)


@dataclass
class CMsgJoinableCustomLobbiesResponseEntry(betterproto.Message):
    lobby_id: float = betterproto.fixed64_field(1)
    custom_game_id: int = betterproto.uint64_field(2)
    lobby_name: str = betterproto.string_field(3)
    member_count: int = betterproto.uint32_field(4)
    leader_account_id: int = betterproto.uint32_field(5)
    leader_name: str = betterproto.string_field(6)
    custom_map_name: str = betterproto.string_field(7)
    max_player_count: int = betterproto.uint32_field(8)
    server_region: int = betterproto.uint32_field(9)
    has_pass_key: bool = betterproto.bool_field(11)
    lan_host_ping_location: str = betterproto.string_field(12)


@dataclass
class CMsgJoinableCustomLobbiesResponse(betterproto.Message):
    lobbies: List["CMsgJoinableCustomLobbiesResponseEntry"] = betterproto.message_field(
        1
    )


@dataclass
class CMsgQuickJoinCustomLobby(betterproto.Message):
    legacy_server_region: int = betterproto.uint32_field(1)
    custom_game_id: int = betterproto.uint64_field(2)
    client_version: int = betterproto.uint32_field(3)
    create_lobby_details: "CMsgPracticeLobbySetDetails" = betterproto.message_field(4)
    allow_any_map: bool = betterproto.bool_field(5)
    legacy_region_pings: List[
        "CMsgQuickJoinCustomLobbyLegacyRegionPing"
    ] = betterproto.message_field(6)
    ping_data: "CMsgClientPingData" = betterproto.message_field(7)


@dataclass
class CMsgQuickJoinCustomLobbyLegacyRegionPing(betterproto.Message):
    server_region: int = betterproto.uint32_field(1)
    ping: int = betterproto.uint32_field(2)
    region_code: float = betterproto.fixed32_field(3)


@dataclass
class CMsgQuickJoinCustomLobbyResponse(betterproto.Message):
    result: "DOTAJoinLobbyResult" = betterproto.enum_field(1)


@dataclass
class CMsgBotGameCreate(betterproto.Message):
    search_key: str = betterproto.string_field(1)
    client_version: int = betterproto.uint32_field(2)
    difficulty_radiant: "DOTABotDifficulty" = betterproto.enum_field(3)
    team: "DOTA_GC_TEAM" = betterproto.enum_field(4)
    game_mode: int = betterproto.uint32_field(5)
    difficulty_dire: "DOTABotDifficulty" = betterproto.enum_field(6)


@dataclass
class CMsgCustomGameCreate(betterproto.Message):
    search_key: str = betterproto.string_field(1)
    client_version: int = betterproto.uint32_field(2)
    difficulty: int = betterproto.uint32_field(3)
    game_mode: str = betterproto.string_field(4)
    map: str = betterproto.string_field(5)
    custom_game_id: int = betterproto.uint64_field(7)


@dataclass
class CMsgEventGameCreate(betterproto.Message):
    search_key: str = betterproto.string_field(1)
    client_version: int = betterproto.uint32_field(2)
    difficulty: int = betterproto.uint32_field(3)
    game_mode: str = betterproto.string_field(4)
    map: str = betterproto.string_field(5)
    custom_game_id: int = betterproto.uint64_field(7)


@dataclass
class CMsgDOTAPartyMemberSetCoach(betterproto.Message):
    wants_coach: bool = betterproto.bool_field(1)


@dataclass
class CMsgDOTASetGroupLeader(betterproto.Message):
    new_leader_steamid: float = betterproto.fixed64_field(1)


@dataclass
class CMsgDOTACancelGroupInvites(betterproto.Message):
    invited_steamids: List[float] = betterproto.fixed64_field(1)
    invited_groupids: List[float] = betterproto.fixed64_field(2)


@dataclass
class CMsgDOTASetGroupOpenStatus(betterproto.Message):
    open: bool = betterproto.bool_field(1)


@dataclass
class CMsgDOTAGroupMergeInvite(betterproto.Message):
    other_group_id: float = betterproto.fixed64_field(1)


@dataclass
class CMsgDOTAGroupMergeResponse(betterproto.Message):
    initiator_group_id: float = betterproto.fixed64_field(1)
    accept: bool = betterproto.bool_field(2)


@dataclass
class CMsgDOTAGroupMergeReply(betterproto.Message):
    result: "EDOTAGroupMergeResult" = betterproto.enum_field(1)


@dataclass
class CMsgSpectatorLobbyGameDetails(betterproto.Message):
    language: int = betterproto.uint32_field(1)
    match_id: int = betterproto.uint64_field(2)
    server_steam_id: float = betterproto.fixed64_field(3)
    stream_url: str = betterproto.string_field(4)
    stream_name: str = betterproto.string_field(5)
    league_id: int = betterproto.uint32_field(6)
    series_type: int = betterproto.uint32_field(7)
    series_game: int = betterproto.uint32_field(8)
    radiant_team: "CMsgSpectatorLobbyGameDetailsTeam" = betterproto.message_field(9)
    dire_team: "CMsgSpectatorLobbyGameDetailsTeam" = betterproto.message_field(10)


@dataclass
class CMsgSpectatorLobbyGameDetailsTeam(betterproto.Message):
    team_id: int = betterproto.uint32_field(1)
    team_name: str = betterproto.string_field(2)
    team_logo: float = betterproto.fixed64_field(3)


@dataclass
class CMsgSetSpectatorLobbyDetails(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    lobby_name: str = betterproto.string_field(2)
    pass_key: str = betterproto.string_field(3)
    game_details: "CMsgSpectatorLobbyGameDetails" = betterproto.message_field(4)


@dataclass
class CMsgCreateSpectatorLobby(betterproto.Message):
    client_version: int = betterproto.uint32_field(1)
    details: "CMsgSetSpectatorLobbyDetails" = betterproto.message_field(2)


@dataclass
class CMsgSpectatorLobbyList(betterproto.Message):
    pass


@dataclass
class CMsgSpectatorLobbyListResponse(betterproto.Message):
    lobbies: List[
        "CMsgSpectatorLobbyListResponseSpectatorLobby"
    ] = betterproto.message_field(1)


@dataclass
class CMsgSpectatorLobbyListResponseSpectatorLobby(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    game_name: str = betterproto.string_field(2)
    requires_pass_key: bool = betterproto.bool_field(3)
    leader_account_id: int = betterproto.uint32_field(4)
    member_count: int = betterproto.uint32_field(5)
    game_details: "CMsgSpectatorLobbyGameDetails" = betterproto.message_field(7)


@dataclass
class CMsgClientToGCRequestSteamDatagramTicket(betterproto.Message):
    server_steam_id: float = betterproto.fixed64_field(1)


@dataclass
class CMsgClientToGCRequestSteamDatagramTicketResponse(betterproto.Message):
    serialized_ticket: bytes = betterproto.bytes_field(1)
    message: str = betterproto.string_field(2)


@dataclass
class CMsgGCToClientSteamDatagramTicket(betterproto.Message):
    legacy_time_expiry: float = betterproto.fixed32_field(1)
    legacy_authorized_steam_id: float = betterproto.fixed64_field(2)
    legacy_authorized_public_ip: float = betterproto.fixed32_field(3)
    legacy_gameserver_steam_id: float = betterproto.fixed64_field(4)
    legacy_gameserver_net_id: float = betterproto.fixed64_field(5)
    legacy_signature: bytes = betterproto.bytes_field(6)
    legacy_app_id: int = betterproto.uint32_field(7)
    legacy_extra_fields: List[bytes] = betterproto.bytes_field(8)
    serialized_ticket: bytes = betterproto.bytes_field(16)


@dataclass
class CMsgGCToClientRequestLaneSelection(betterproto.Message):
    pass


@dataclass
class CMsgGCToClientRequestLaneSelectionResponse(betterproto.Message):
    lane_selection_flags: int = betterproto.uint32_field(1)
    high_priority_disabled: bool = betterproto.bool_field(2)


@dataclass
class CMsgGCToClientRequestMMInfo(betterproto.Message):
    pass


@dataclass
class CMsgClientToGCMMInfo(betterproto.Message):
    lane_selection_flags: int = betterproto.uint32_field(1)
    high_priority_disabled: bool = betterproto.bool_field(2)
