# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_gcmessages_common_match_management.proto
# plugin: python-betterproto

from dataclasses import dataclass
from typing import List

import betterproto

from .dota_gcmessages_common import CMsgLobbyEventPoints
from .dota_shared_enums import (
    CDOTASaveGame,
    CMsgPendingEventAward,
    DOTABotDifficulty,
    DOTACMPick,
    DOTAGCTeam,
    DOTAGameState,
    DOTAGameVersion,
    DOTALeaverStatus,
    DOTALobbyVisibility,
    DOTASelectionPriorityChoice,
    DOTASelectionPriorityRules,
    EDOTAMMRBoostType,
    EEvent,
    EMatchOutcome,
    ETourneyQueueDeadlineState,
    MatchType,
)
from .gcsdk_gcmessages import PartnerAccountType


class ELaneSelection(betterproto.Enum):
    Safelane = 0
    Offlane = 1
    Midlane = 2
    SupportSoft = 3
    SupportHard = 4


class ELaneSelectionFlags(betterproto.Enum):
    NONE = 0
    Safelane = 1
    Offlane = 2
    Midlane = 4
    Core = 7
    SupportSoft = 8
    SupportHard = 16
    Support = 24
    All = 31


class EPartyMatchmakingFlags(betterproto.Enum):
    NONE = 0
    LargeRankSpread = 1


class EHighPriorityMMState(betterproto.Enum):
    Unknown = 0
    MissingMMData = 1
    ResourceMissing = 2
    ManuallyDisabled = 3
    Min_Enabled = 64
    AllRolesSelected = 65
    UsingResource = 66
    FiveStack = 67
    HighDemand = 68


class LobbyDotaTVDelay(betterproto.Enum):
    LobbyDotaTV_10 = 0
    LobbyDotaTV_120 = 1
    LobbyDotaTV_300 = 2


class LobbyDotaPauseSetting(betterproto.Enum):
    Unlimited = 0
    Limited = 1
    Disabled = 2


class EReadyCheckStatus(betterproto.Enum):
    Unknown = 0
    NotReady = 1
    Ready = 2


class EReadyCheckRequestResult(betterproto.Enum):
    Success = 0
    AlreadyInProgress = 1
    NotInParty = 2
    SendError = 3
    UnknownError = 4


class EMatchBehaviorScoreVariance(betterproto.Enum):
    Invalid = 0
    Low = 1
    Medium = 2
    High = 3


class CSODOTAPartyState(betterproto.Enum):
    UI = 0
    FINDING_MATCH = 1
    IN_MATCH = 2


class CSODOTALobbyState(betterproto.Enum):
    UI = 0
    Readyup = 4
    Serversetup = 1
    Run = 2
    Postgame = 3
    Notready = 5
    Serverassign = 6


class CSODOTALobbyLobbyType(betterproto.Enum):
    Invalid = -1
    CasualMatch = 0
    Practice = 1
    CoopBotMatch = 4
    LegacyTeamMatch = 5
    LegacySoloQueueMatch = 6
    CompetitiveMatch = 7
    Casual1V1Match = 8
    WeekendTourney = 9
    LocalBotMatch = 10
    Spectator = 11
    EventMatch = 12
    Gauntlet = 13


class CMvpDataAccoladeMvpAccoladeType(betterproto.Enum):
    Kills = 1
    Deaths = 2
    Assists = 3
    NetWorth = 5
    ItemValue = 6
    SupportGoldSpent = 7
    WardsPlaced = 8
    Dewards = 9
    CampsStacked = 10
    LastHits = 11
    Denies = 12
    KillingSprees = 13
    Godlike = 14
    TowersDestroyed = 15
    InvokerSunstrikeKills = 16
    AxeCulls = 17
    AxeBattleHungerKills = 18
    LowHealthKills = 19
    InvokerTornadoKills = 20
    SvenDoubleStuns = 21
    SvenWarcryAssists = 22
    SvenCleaveDoubleKills = 23
    SvenTeleportInterrupts = 24
    FacelessMultiChrono = 25
    FacelessChronoKills = 26
    UrsaMultiShocks = 27
    RoshanKills = 28
    LionFingerKills = 29
    RikiSmokedHeroKills = 32
    HeroesRevealedWithDust = 33
    SkeletonKingReincarnationKills = 34
    SkywrathFlareKills = 35
    LeshracSplitEarthStuns = 36
    MiranaMaxStunArrows = 37
    PhantomAssassinCoupdeGraceCrits = 38
    PhantomAssassinDaggerCrits = 39
    MeepoEarthbinds = 40
    BloodseekerRuptureKills = 41
    SlarkLeashedEnemies = 42
    DisruptorFountainGlimpses = 43
    RubickSpellsStolen = 44
    RubickUltimatesStolen = 45
    DoomEnemiesDoomed = 46
    OmniknightPurifications = 47
    OmniknightAlliesRepelled = 48
    OmniknightEnemiesRepelled = 49
    WarlockFiveHeroFatalBonds = 50
    CrystalMaidenFrostbittenEnemies = 51
    CrystalMaidenCrystalNovas = 52
    KunkkaDoubleHeroTorrents = 53
    KunkkaTripleHeroGhostShips = 54
    NagaSirenEnemiesEnsnared = 55
    NagaSirenTripleHeroRipTides = 56
    LycanKillsDuringShapeshift = 57
    PudgeDismemberKills = 58
    PudgeEnemyHeroesHooked = 59
    PudgeHookKills = 60
    PudgeUnseenEnemyHeroesHooked = 61
    DrowRangerEnemiesSilenced = 62
    DrowRangerMultiHeroSilences = 63
    DrowRangerSilencedKills = 64
    DrowRangerFrostArrowKills = 65
    DragonKnightKillsInDragonForm = 66
    DragonKnightBreatheFireKills = 67
    DragonKnightSplashKills = 68
    WitchDoctorCaskStuns = 69
    WitchDoctorMaledictKills = 70
    WitchDoctorMultiHeroMaledicts = 71
    WitchDoctorDeathWardKills = 72
    DisruptorThunderStrikeKills = 73
    DisruptorHeroesGlimpsed = 74
    CrystalMaidenFreezingFieldKills = 75
    MedusaEnemiesPetrified = 77
    WarlockFatalBondsKills = 78
    WarlockGolemKills = 79
    TuskWalrusPunches = 80
    TuskSnowballStuns = 81
    EarthshakerFissureStuns = 82
    Earthshaker3HeroEchoslams = 83
    SandKingBurrowstrikeStuns = 84
    SandKingEpicenterKills = 85
    SkywrathMageAncientSealKills = 86
    SkywrathMageConcussiveShotKills = 87
    LunaLucentBeamKills = 88
    LunaEclipseKills = 89
    KeeperOfTheLightIlluminateKills = 90
    KeeperOfTheLightManaLeakStuns = 91
    KeeperOfTheLightTeammatesRecalled = 92
    LegionCommanderDuelsWon = 93
    BeastmasterRoarKills = 94
    BeastmasterRoarMultiKills = 95
    WindrunnerFocusFireBuildings = 96
    WindrunnerPowershotKills = 97
    PhantomAssassinDaggerLastHits = 98
    PhantomAssassinPhantomStrikeKills = 99
    DeathProphetCryptSwarmKills = 100
    DeathProphetExorcismBuildingKills = 101
    DeathProphetExorcismSpiritsSummoned = 102
    DeathProphetMultiHeroSilences = 103
    AbaddonMistCoilKills = 104
    AbaddonMistCoilHealed = 105
    AbaddonAphoticShieldKills = 106
    LichChainFrostTripleKills = 107
    LichChainFrostMultiKills = 108
    LichChainFrostBounces = 109
    UrsaEnragedKills = 110
    UrsaEarthshockKills = 111
    LinaLagunaBladeKills = 112
    LinaDragonSlaveKills = 113
    LinaLightStrikeArrayStuns = 114
    BarracksDestroyed = 115
    TemplarAssassinMeldKills = 116
    TemplarAssassinHeroesSlowed = 117
    SniperAssassinationKills = 118
    SniperHeadshotStuns = 119
    EarthSpiritSmashStuns = 120
    EarthSpiritGripSilences = 121
    ShadowShamanShackleKills = 122
    ShadowShamanHexKills = 123
    CentaurEnemiesStomped = 124
    CentaurDoubleEdgeKills = 125
    CentaurReturnKills = 126
    EmberSpiritEnemiesChained = 127
    EmberSpiritSleightOfFistMultiKills = 128
    PuckOrbKills = 129
    VengefulSpiritEnemiesStunned = 130
    LifestealerRageKills = 131
    LifestealerOpenWoundsKills = 132
    LifestealerInfestKills = 133
    ElderTitanSpiritKills = 134
    ElderTitanGoodStomps = 135
    ClockwerkRocketKills = 136
    ClockwerkBlindRocketKills = 137
    StormSpiritBallKills = 138
    StormSpiritDoubleRemnantKills = 139
    StormSpiritVortexKills = 140
    TinkerDoubleMissileKills = 141
    TinkerLaserKills = 142
    TechiesSuicideKills = 143
    TechiesLandMineKills = 144
    TechiesStatisTrapStuns = 145
    TechiesRemoteMineKills = 146
    ShadowFiendTripleRazeKills = 147
    ShadowFiendRequiemMultiKills = 148
    ShadowFiendQRazeKills = 149
    ShadowFiendWRazeKills = 150
    ShadowFiendERazeKills = 151
    OracleFatesEdictKills = 152
    OracleFalsePromiseSaves = 153
    JuggernautOmnislashKills = 154
    SkeletonKingSkeletonHeroKills = 157
    DarkWillowCursedCrownTripleStuns = 158
    DazzleShallowGraveSaves = 159
    DazzlePoisonTouchKills = 160
    ThreeManMeks = 161
    ViperPoisonAttackKills = 162
    ViperCorrosiveSkinKills = 163
    ThreeHeroVeils = 164
    ViperKillsDuringViperStrike = 165
    SolarCrestKills = 166
    TinyTreeThrowKills = 167
    RikiBackstabKills = 168
    PhoenixThreeHeroSupernovaStuns = 169
    TerrorbladeMetamorphosisKills = 170
    LionGreatFingerKills = 171
    AntimageSpellsBlockedWithAghanims = 172
    AntimageThreeManManaVoids = 173
    ArcWardenTempestDoubleKills = 174
    ArcWardenSparkWraithKills = 175
    BaneBrainSapKills = 176
    BaneFiendsGripKills = 177
    BatriderTripleHeroFlamebreaks = 178
    BatriderDoubleHeroLassoes = 179
    BrewmasterKillsDuringPrimalSplit = 180
    BristlebackKillsUnderFourQuillStacks = 181
    BristlebackTripleHeroNasalGoo = 182
    BroodmotherSpiderlingHeroKills = 183
    BroodmotherKillsInsideWeb = 184
    CentaurThreeHeroStampede = 185
    ChaosKnightRealityRiftKills = 186
    ChenKillsWithPenitence = 187
    CrystalMaidenTwoHeroCrystalNovas = 188
    CrystalMaidenThreeHeroFreezingFields = 189
    DazzleShadowWaveKills = 190
    DeathProphetSiphonKills = 191
    DeathProphetExorcismKillsDuringEuls = 192
    DisruptorThreeHeroKineticFieldStaticStorm = 193
    DoomInfernalBladeBurnKills = 194
    DrowRangerPrecisionAuraCreepTowerKills = 195
    EmberSpiritRemnantKills = 196
    EmberSpiritSleightOfFistKills = 197
    EnigmaMidnightPulseBlackHoleCombos = 198
    EnigmaThreeManBlackHoles = 199
    FacelessVoidMultiHeroTimeDilation = 200
    GyrocopterThreeHeroFlakCannon = 201
    GyrocopterHomingMissileKills = 202
    GyrocopterRocketBarrageKills = 203
    HuskarKillsDuringLifeBreak = 204
    HuskarBurningSpearKills = 205
    InvokerMultiHeroIceWall = 206
    InvokerThreeHeroEmp = 207
    InvokerThreeHeroDeafeningBlast = 208
    InvokerMultiHeroChaosMeteor = 209
    JakiroMultiHeroDualBreath = 210
    JakiroIcePathMacropyreCombos = 211
    LeshracPulseNovaKills = 212
    LeshracThreeHeroLightningStorm = 213
    LionThreeHeroFingerOfDeath = 214
    MeepoPoofKills = 215
    MeepoMultiHeroEarthbinds = 216
    NightStalkerNighttimeKills = 217
    MorphlingKillsDuringReplicate = 218
    OgreMagiFireblastKills = 219
    OgreMagiIgniteKills = 220
    DominatingKillStreaks = 221
    MegaKillStreaks = 222
    AlchemistAghanimsGiven = 223
    VeilsLeadingToKills = 224
    DustLeadingToKills = 225
    WitchDoctorMultiHeroCaskStuns = 226
    WeaverShukuchiKills = 227
    WindrunnerShackleFocusFireKills = 228
    VengefulSpiritVengeanceAuraIllusionKills = 229
    TuskWalrusPunchKills = 230
    TinkerTripleHeroLasers = 231
    TemplarAssassinMultiHeroPsiBlades = 232
    SvenKillsDuringGodsStrength = 233
    SniperThreeHeroShrapnels = 234
    SlarkKillsDuringShadowDance = 235
    ShadowShamanMultiHeroEtherShocks = 236
    ShadowShamanSerpentWardShackleKills = 237
    RikiThreeHeroTricksOfTheTrade = 238
    RazorEyeOfTheStormKills = 239
    PugnaLifeDrainKills = 240
    ObsidianDestroyerSanitysEclipseKills = 241
    OracleMultiHeroFortunesEnd = 242
    OmniknightPurificationKills = 243
    NightStalkerEnemyMissesUnderCripplingFear = 244
    WarlockThreeHeroFatalBonds = 245
    RikiTricksOfTheTradeKills = 246
    EarthshakerAftershockHits10 = 247
    Earthshaker5HeroEchoslams = 248
    LinaLagunaBladeHeroKills = 249
    LinaLightStrikeHeroStuns = 250
    EarthshakerFissureMultiStuns = 251
    EarthshakerTotemKills = 252
    PangolierSwashbuckleKills = 253
    FurionEnemyHeroesTrapped = 254
    PangolierHeartpiercerKills = 255
    MedusaMultiHeroStoneGaze = 256
    MedusaSplitShotKills = 257
    MiranaMultiHeroStarstorm = 258
    MiranaKillsFromMoonlightShadow = 259
    MagnusMultiHeroSkewers = 260
    MagnusMultiHeroReversePolarity = 261
    MagnusHeroesSlowedWithShockwave = 262
    NagaSirenMultiHeroSong = 263
    NagaSirenAlliesHealedBySong = 264
    LoneDruidMultiHeroRoar = 265
    LoneDruidBattleCryKills = 266
    WinterWyvernThreeHeroCurses = 267
    AntimageSpellsBlockedWithCounterspell = 268
    MarsEnemiesKilledInArena = 269
    MarsMultiHeroGodsRebuke = 270
    MarsGodsRebukeKills = 271
    SnapfireLizardBlobsKills = 272
    SnapfireTwoHeroCookieStuns = 273
    CustomKillStreak = 274


@dataclass(eq=False, repr=False)
class CSODOTAPartyMember(betterproto.Message):
    partner_type: "PartnerAccountType" = betterproto.enum_field(1)
    is_coach: bool = betterproto.bool_field(2)
    region_ping_codes: List[int] = betterproto.uint32_field(4)
    region_ping_times: List[int] = betterproto.uint32_field(5)
    region_ping_failed_bitmask: int = betterproto.uint32_field(6)
    is_plus_subscriber: bool = betterproto.bool_field(10)
    tourney_skill_level: int = betterproto.uint32_field(7)
    tourney_buyin: int = betterproto.uint32_field(8)
    tourney_prevent_until: int = betterproto.uint32_field(9)
    mm_data_valid: bool = betterproto.bool_field(13)
    lane_selection_flags: int = betterproto.uint32_field(11)
    high_priority_disabled: bool = betterproto.bool_field(14)
    has_hp_resource: bool = betterproto.bool_field(15)
    joined_from_partyfinder: bool = betterproto.bool_field(12)


@dataclass(eq=False, repr=False)
class CSODOTAParty(betterproto.Message):
    party_id: int = betterproto.uint64_field(1)
    leader_id: float = betterproto.fixed64_field(2)
    member_ids: List[float] = betterproto.fixed64_field(3)
    game_modes: int = betterproto.uint32_field(4)
    state: "CSODOTAPartyState" = betterproto.enum_field(6)
    effective_started_matchmaking_time: int = betterproto.uint32_field(7)
    raw_started_matchmaking_time: int = betterproto.uint32_field(32)
    attempt_start_time: int = betterproto.uint32_field(33)
    attempt_num: int = betterproto.uint32_field(34)
    matchgroups: int = betterproto.uint32_field(11)
    low_priority_account_id: int = betterproto.uint32_field(19)
    match_type: "MatchType" = betterproto.enum_field(21)
    bot_difficulty: "DOTABotDifficulty" = betterproto.enum_field(22)
    team_id: int = betterproto.uint32_field(23)
    team_name: str = betterproto.string_field(51)
    team_ui_logo: int = betterproto.uint64_field(52)
    team_base_logo: int = betterproto.uint64_field(53)
    match_disabled_until_date: int = betterproto.uint32_field(24)
    match_disabled_account_id: int = betterproto.uint32_field(25)
    matchmaking_max_range_minutes: int = betterproto.uint32_field(26)
    matchlanguages: int = betterproto.uint32_field(27)
    members: List["CSODOTAPartyMember"] = betterproto.message_field(29)
    low_priority_games_remaining: int = betterproto.uint32_field(35)
    open_for_join_requests: bool = betterproto.bool_field(40)
    sent_invites: List["CSODOTAPartyInvite"] = betterproto.message_field(41)
    recv_invites: List["CSODOTAPartyInvite"] = betterproto.message_field(42)
    account_flags: int = betterproto.uint32_field(43)
    region_select_flags: int = betterproto.uint32_field(44)
    exclusive_tournament_id: int = betterproto.uint32_field(45)
    tourney_division_id: int = betterproto.uint32_field(47)
    tourney_schedule_time: int = betterproto.uint32_field(48)
    tourney_skill_level: int = betterproto.uint32_field(49)
    tourney_bracket_round: int = betterproto.uint32_field(50)
    tourney_queue_deadline_time: int = betterproto.uint32_field(54)
    tourney_queue_deadline_state: "ETourneyQueueDeadlineState" = betterproto.enum_field(55)
    party_builder_slots_to_fill: int = betterproto.uint32_field(56)
    party_builder_match_groups: int = betterproto.uint32_field(57)
    party_builder_start_time: int = betterproto.uint32_field(58)
    solo_queue: bool = betterproto.bool_field(59)
    bot_script_index: int = betterproto.uint32_field(60)
    steam_clan_account_id: int = betterproto.uint32_field(61)
    ready_check: "CMsgReadyCheckStatus" = betterproto.message_field(62)
    custom_game_disabled_until_date: int = betterproto.uint32_field(63)
    custom_game_disabled_account_id: int = betterproto.uint32_field(64)
    is_challenge_match: bool = betterproto.bool_field(65)
    party_search_beacon_active: bool = betterproto.bool_field(66)
    matchmaking_flags: int = betterproto.uint32_field(67)
    high_priority_state: "EHighPriorityMMState" = betterproto.enum_field(68)
    lane_selections_enabled: bool = betterproto.bool_field(69)
    custom_game_difficulty_mask: int = betterproto.uint32_field(70)


@dataclass(eq=False, repr=False)
class CSODOTAPartyInvite(betterproto.Message):
    group_id: int = betterproto.uint64_field(1)
    sender_id: float = betterproto.fixed64_field(2)
    sender_name: str = betterproto.string_field(3)
    members: List["CSODOTAPartyInvitePartyMember"] = betterproto.message_field(4)
    team_id: int = betterproto.uint32_field(5)
    low_priority_status: bool = betterproto.bool_field(6)
    as_coach: bool = betterproto.bool_field(7)
    invite_gid: float = betterproto.fixed64_field(8)


@dataclass(eq=False, repr=False)
class CSODOTAPartyInvitePartyMember(betterproto.Message):
    name: str = betterproto.string_field(1)
    steam_id: float = betterproto.fixed64_field(2)
    is_coach: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class CSODOTALobbyInvite(betterproto.Message):
    group_id: int = betterproto.uint64_field(1)
    sender_id: float = betterproto.fixed64_field(2)
    sender_name: str = betterproto.string_field(3)
    members: List["CSODOTALobbyInviteLobbyMember"] = betterproto.message_field(4)
    custom_game_id: int = betterproto.uint64_field(5)
    invite_gid: float = betterproto.fixed64_field(6)
    custom_game_crc: float = betterproto.fixed64_field(7)
    custom_game_timestamp: float = betterproto.fixed32_field(8)


@dataclass(eq=False, repr=False)
class CSODOTALobbyInviteLobbyMember(betterproto.Message):
    name: str = betterproto.string_field(1)
    steam_id: float = betterproto.fixed64_field(2)


@dataclass(eq=False, repr=False)
class CMsgLeaverState(betterproto.Message):
    lobby_state: int = betterproto.uint32_field(1)
    game_state: "DOTAGameState" = betterproto.enum_field(2)
    leaver_detected: bool = betterproto.bool_field(3)
    first_blood_happened: bool = betterproto.bool_field(4)
    discard_match_results: bool = betterproto.bool_field(5)
    mass_disconnect: bool = betterproto.bool_field(6)


@dataclass(eq=False, repr=False)
class CSODOTALobbyMember(betterproto.Message):
    id: float = betterproto.fixed64_field(1)
    hero_id: int = betterproto.uint32_field(2)
    team: "DOTAGCTeam" = betterproto.enum_field(3)
    name: str = betterproto.string_field(6)
    slot: int = betterproto.uint32_field(7)
    party_id: int = betterproto.uint64_field(12)
    meta_level: int = betterproto.uint32_field(13)
    meta_xp: int = betterproto.uint32_field(14)
    meta_xp_awarded: int = betterproto.uint32_field(15)
    leaver_status: "DOTALeaverStatus" = betterproto.enum_field(16)
    leaver_actions: int = betterproto.uint32_field(28)
    channel: int = betterproto.uint32_field(17)
    disabled_hero_id: List[int] = betterproto.uint32_field(20)
    partner_account_type: "PartnerAccountType" = betterproto.enum_field(21)
    enabled_hero_id: List[int] = betterproto.uint32_field(22)
    coach_team: "DOTAGCTeam" = betterproto.enum_field(23)
    coach_rating: int = betterproto.uint32_field(42)
    pwrd_cyber_cafe_id: int = betterproto.uint32_field(24)
    pwrd_cyber_cafe_name: str = betterproto.string_field(25)
    disabled_random_hero_bits: List[float] = betterproto.fixed32_field(41)
    rank_change: int = betterproto.sint32_field(29)
    cameraman: bool = betterproto.bool_field(30)
    custom_game_product_ids: List[int] = betterproto.uint32_field(31)
    search_match_type: "MatchType" = betterproto.enum_field(33)
    favorite_team_packed: int = betterproto.uint64_field(35)
    is_plus_subscriber: bool = betterproto.bool_field(36)
    rank_tier_updated: bool = betterproto.bool_field(37)
    lane_selection_flags: int = betterproto.uint32_field(38)
    can_earn_rewards: bool = betterproto.bool_field(39)
    live_spectator_team: "DOTAGCTeam" = betterproto.enum_field(40)
    was_mvp_last_game: bool = betterproto.bool_field(43)
    pending_awards: List["CMsgPendingEventAward"] = betterproto.message_field(44)
    pending_awards_on_victory: List["CMsgPendingEventAward"] = betterproto.message_field(45)
    rank_mmr_boost_type: "EDOTAMMRBoostType" = betterproto.enum_field(46)
    queue_point_adjustment: int = betterproto.sint32_field(47)
    rank_tier: int = betterproto.int32_field(48)
    title: int = betterproto.uint32_field(50)
    guild_id: int = betterproto.uint32_field(51)


@dataclass(eq=False, repr=False)
class CLobbyTeamDetails(betterproto.Message):
    team_name: str = betterproto.string_field(1)
    team_tag: str = betterproto.string_field(3)
    team_id: int = betterproto.uint32_field(4)
    team_logo: int = betterproto.uint64_field(5)
    team_base_logo: int = betterproto.uint64_field(6)
    team_banner_logo: int = betterproto.uint64_field(7)
    team_complete: bool = betterproto.bool_field(8)
    rank: int = betterproto.uint32_field(15)
    rank_change: int = betterproto.sint32_field(16)
    is_home_team: bool = betterproto.bool_field(17)
    is_challenge_match: bool = betterproto.bool_field(18)
    challenge_match_token_account: int = betterproto.uint64_field(19)
    team_logo_url: str = betterproto.string_field(20)


@dataclass(eq=False, repr=False)
class CLobbyGuildDetails(betterproto.Message):
    guild_id: int = betterproto.uint32_field(1)
    guild_primary_color: int = betterproto.uint32_field(2)
    guild_secondary_color: int = betterproto.uint32_field(3)
    guild_pattern: int = betterproto.uint32_field(4)
    guild_logo: int = betterproto.uint64_field(5)
    guild_points: int = betterproto.uint32_field(6)
    guild_event: int = betterproto.uint32_field(7)
    guild_flags: int = betterproto.uint32_field(8)
    team_for_guild: "DOTAGCTeam" = betterproto.enum_field(9)
    guild_tag: str = betterproto.string_field(10)


@dataclass(eq=False, repr=False)
class CLobbyTimedRewardDetails(betterproto.Message):
    item_def_index: int = betterproto.uint32_field(2)
    is_supply_crate: bool = betterproto.bool_field(3)
    is_timed_drop: bool = betterproto.bool_field(4)
    account_id: int = betterproto.uint32_field(5)
    origin: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class CLobbyBroadcastChannelInfo(betterproto.Message):
    channel_id: int = betterproto.uint32_field(1)
    country_code: str = betterproto.string_field(2)
    description: str = betterproto.string_field(3)
    language_code: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class CLobbyGuildChallenge(betterproto.Message):
    guild_id: int = betterproto.uint32_field(1)
    event_id: "EEvent" = betterproto.enum_field(2)
    challenge_instance_id: int = betterproto.uint32_field(3)
    challenge_parameter: int = betterproto.uint32_field(4)
    challenge_timestamp: int = betterproto.uint32_field(5)
    challenge_period_serial: int = betterproto.uint32_field(6)
    challenge_progress_at_start: int = betterproto.uint32_field(7)
    eligible_account_ids: List[int] = betterproto.uint32_field(8)


@dataclass(eq=False, repr=False)
class CSODOTALobby(betterproto.Message):
    lobby_id: int = betterproto.uint64_field(1)
    members: List["CSODOTALobbyMember"] = betterproto.message_field(2)
    left_members: List["CSODOTALobbyMember"] = betterproto.message_field(7)
    leader_id: float = betterproto.fixed64_field(11)
    server_id: float = betterproto.fixed64_field(6)
    game_mode: int = betterproto.uint32_field(3)
    pending_invites: List[float] = betterproto.fixed64_field(10)
    state: "CSODOTALobbyState" = betterproto.enum_field(4)
    connect: str = betterproto.string_field(5)
    lobby_type: "CSODOTALobbyLobbyType" = betterproto.enum_field(12)
    allow_cheats: bool = betterproto.bool_field(13)
    fill_with_bots: bool = betterproto.bool_field(14)
    intro_mode: bool = betterproto.bool_field(15)
    game_name: str = betterproto.string_field(16)
    team_details: List["CLobbyTeamDetails"] = betterproto.message_field(17)
    tutorial_lesson: int = betterproto.uint32_field(18)
    tournament_id: int = betterproto.uint32_field(19)
    tournament_game_id: int = betterproto.uint32_field(20)
    server_region: int = betterproto.uint32_field(21)
    game_state: "DOTAGameState" = betterproto.enum_field(22)
    num_spectators: int = betterproto.uint32_field(23)
    matchgroup: int = betterproto.uint32_field(25)
    cm_pick: "DOTACMPick" = betterproto.enum_field(28)
    match_id: int = betterproto.uint64_field(30)
    allow_spectating: bool = betterproto.bool_field(31)
    bot_difficulty_radiant: "DOTABotDifficulty" = betterproto.enum_field(36)
    game_version: "DOTAGameVersion" = betterproto.enum_field(37)
    timed_reward_details: List["CLobbyTimedRewardDetails"] = betterproto.message_field(38)
    pass_key: str = betterproto.string_field(39)
    leagueid: int = betterproto.uint32_field(42)
    penalty_level_radiant: int = betterproto.uint32_field(43)
    penalty_level_dire: int = betterproto.uint32_field(44)
    load_game_id: int = betterproto.uint32_field(45)
    series_type: int = betterproto.uint32_field(46)
    radiant_series_wins: int = betterproto.uint32_field(47)
    dire_series_wins: int = betterproto.uint32_field(48)
    loot_generated: int = betterproto.uint32_field(49)
    loot_awarded: int = betterproto.uint32_field(50)
    allchat: bool = betterproto.bool_field(51)
    dota_tv_delay: "LobbyDotaTVDelay" = betterproto.enum_field(53)
    custom_game_mode: str = betterproto.string_field(54)
    custom_map_name: str = betterproto.string_field(55)
    custom_difficulty: int = betterproto.uint32_field(56)
    lan: bool = betterproto.bool_field(57)
    broadcast_channel_info: List["CLobbyBroadcastChannelInfo"] = betterproto.message_field(58)
    first_leaver_accountid: int = betterproto.uint32_field(59)
    series_id: int = betterproto.uint32_field(60)
    low_priority: bool = betterproto.bool_field(61)
    extra_messages: List["CSODOTALobbyCExtraMsg"] = betterproto.message_field(62)
    save_game: "CDOTASaveGame" = betterproto.message_field(63)
    first_blood_happened: bool = betterproto.bool_field(65)
    match_outcome: "EMatchOutcome" = betterproto.enum_field(70)
    mass_disconnect: bool = betterproto.bool_field(67)
    custom_game_id: int = betterproto.uint64_field(68)
    custom_min_players: int = betterproto.uint32_field(71)
    custom_max_players: int = betterproto.uint32_field(72)
    partner_type: "PartnerAccountType" = betterproto.enum_field(73)
    visibility: "DOTALobbyVisibility" = betterproto.enum_field(75)
    custom_game_crc: float = betterproto.fixed64_field(76)
    custom_game_auto_created_lobby: bool = betterproto.bool_field(77)
    custom_game_timestamp: float = betterproto.fixed32_field(80)
    previous_series_matches: List[int] = betterproto.uint64_field(81)
    previous_match_override: int = betterproto.uint64_field(82)
    custom_game_uses_account_records: bool = betterproto.bool_field(83)
    game_start_time: int = betterproto.uint32_field(87)
    pause_setting: "LobbyDotaPauseSetting" = betterproto.enum_field(88)
    lobby_mvp_account_id: int = betterproto.uint32_field(89)
    weekend_tourney_division_id: int = betterproto.uint32_field(90)
    weekend_tourney_skill_level: int = betterproto.uint32_field(91)
    weekend_tourney_bracket_round: int = betterproto.uint32_field(92)
    bot_difficulty_dire: "DOTABotDifficulty" = betterproto.enum_field(93)
    bot_radiant: int = betterproto.uint64_field(94)
    bot_dire: int = betterproto.uint64_field(95)
    event_progression_enabled: List["EEvent"] = betterproto.enum_field(96)
    selection_priority_rules: "DOTASelectionPriorityRules" = betterproto.enum_field(97)
    series_previous_selection_priority_team_id: int = betterproto.uint32_field(98)
    series_current_selection_priority_team_id: int = betterproto.uint32_field(99)
    series_current_priority_team_choice: "DOTASelectionPriorityChoice" = betterproto.enum_field(100)
    series_current_non_priority_team_choice: "DOTASelectionPriorityChoice" = betterproto.enum_field(101)
    series_current_selection_priority_used_coin_toss: bool = betterproto.bool_field(102)
    current_primary_event: "EEvent" = betterproto.enum_field(103)
    emergency_disabled_hero_ids: List[int] = betterproto.uint32_field(105)
    custom_game_private_key: float = betterproto.fixed64_field(106)
    custom_game_penalties: bool = betterproto.bool_field(107)
    lan_host_ping_location: str = betterproto.string_field(109)
    league_node_id: int = betterproto.uint32_field(110)
    match_duration: int = betterproto.uint32_field(111)
    custom_game_browseable: bool = betterproto.bool_field(112)
    league_phase: int = betterproto.uint32_field(113)
    record_detailed_stats: bool = betterproto.bool_field(114)
    experimental_gameplay_enabled: bool = betterproto.bool_field(116)
    guild_challenges: List["CLobbyGuildChallenge"] = betterproto.message_field(117)
    guild_details: List["CLobbyGuildDetails"] = betterproto.message_field(118)
    lobby_event_points: List["CMsgLobbyEventPoints"] = betterproto.message_field(119)


@dataclass(eq=False, repr=False)
class CSODOTALobbyCExtraMsg(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    contents: bytes = betterproto.bytes_field(2)


@dataclass(eq=False, repr=False)
class CMsgLobbyPlaytestDetails(betterproto.Message):
    json: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class CMsgReadyCheckStatus(betterproto.Message):
    start_timestamp: int = betterproto.uint32_field(1)
    finish_timestamp: int = betterproto.uint32_field(2)
    initiator_account_id: int = betterproto.uint32_field(3)
    ready_members: List["CMsgReadyCheckStatusReadyMember"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class CMsgReadyCheckStatusReadyMember(betterproto.Message):
    account_id: int = betterproto.uint32_field(1)
    ready_status: "EReadyCheckStatus" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class CMsgPartyReadyCheckRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class CMsgPartyReadyCheckResponse(betterproto.Message):
    result: "EReadyCheckRequestResult" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class CMsgPartyReadyCheckAcknowledge(betterproto.Message):
    ready_status: "EReadyCheckStatus" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class CMsgLobbyEventGameDetails(betterproto.Message):
    kv_data: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class CMsgMatchMatchmakingStats(betterproto.Message):
    average_queue_time: int = betterproto.uint32_field(1)
    maximum_queue_time: int = betterproto.uint32_field(2)
    behavior_score_variance: "EMatchBehaviorScoreVariance" = betterproto.enum_field(3)
