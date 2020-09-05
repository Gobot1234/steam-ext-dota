# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: dota_shared_enums.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


class DOTAGameMode(betterproto.Enum):
    NONE = 0
    Ap = 1
    Cm = 2
    Rd = 3
    Sd = 4
    Ar = 5
    Intro = 6
    Hw = 7
    ReverseCm = 8
    Xmas = 9
    Tutorial = 10
    Mo = 11
    Lp = 12
    Pool1 = 13
    Fh = 14
    Custom = 15
    Cd = 16
    Bd = 17
    AbilityDraft = 18
    Event = 19
    Ardm = 20
    _1v1Mid = 21
    AllDraft = 22
    Turbo = 23
    Mutation = 24
    CoachesChallenge = 25


class DOTAGameState(betterproto.Enum):
    Init = 0
    WaitForPlayersToLoad = 1
    HeroSelection = 2
    StrategyTime = 3
    PreGame = 4
    GameInProgress = 5
    PostGame = 6
    Disconnect = 7
    TeamShowcase = 8
    CustomGameSetup = 9
    WaitForMapToLoad = 10
    Last = 11


class DOTAGCTeam(betterproto.Enum):
    GoodGuys = 0
    BadGuys = 1
    Broadcaster = 2
    Spectator = 3
    PlayerPool = 4
    NoTeam = 5


class EEvent(betterproto.Enum):
    NONE = 0
    Diretide = 1
    SpringFestival = 2
    Frostivus2013 = 3
    Compendium2014 = 4
    NexonPCBang = 5
    PWRDDac2015 = 6
    NewBloom2015 = 7
    International2015 = 8
    FallMajor2015 = 9
    OraclePa = 10
    NewBloom2015Prebeast = 11
    Frostivus = 12
    WinterMajor2016 = 13
    International2016 = 14
    FallMajor2016 = 15
    WinterMajor2017 = 16
    NewBloom2017 = 17
    International2017 = 18
    PlusSubscription = 19
    SinglesDay2017 = 20
    Frostivus2017 = 21
    International2018 = 22
    Frostivus2018 = 23
    NewBloom2019 = 24
    International2019 = 25
    NewPlayerExperience = 26
    Frostivus2019 = 27
    NewBloom2020 = 28
    International2020 = 29
    TeamFandom = 30
    Count = 31


class DOTALeaverStatusT(betterproto.Enum):
    NONE = 0
    Disconnected = 1
    DisconnectedTooLong = 2
    Abandoned = 3
    Afk = 4
    NeverConnected = 5
    NeverConnectedTooLong = 6
    FailedToReadyUp = 7
    Declined = 8


class DOTAConnectionStateT(betterproto.Enum):
    Unknown = 0
    NotYetConnected = 1
    Connected = 2
    Disconnected = 3
    Abandoned = 4
    Loading = 5
    Failed = 6


class FantasyRoles(betterproto.Enum):
    Undefined = 0
    Core = 1
    Support = 2
    Offlane = 3
    Mid = 4


class FantasyTeamSlots(betterproto.Enum):
    NONE = 0
    Core = 1
    Support = 2
    Any = 3
    Bench = 4


class FantasySelectionMode(betterproto.Enum):
    Invalid = 0
    Locked = 1
    Shuffle = 2
    FreePick = 3
    Ended = 4
    PreSeason = 5
    PreDraft = 6
    Drafting = 7
    RegularSeason = 8
    CardBased = 9


class DOTAChatChannelType(betterproto.Enum):
    Regional = 0
    Custom = 1
    Party = 2
    Lobby = 3
    Team = 4
    Guild = 5
    Fantasy = 6
    Whisper = 7
    Console = 8
    Tab = 9
    Invalid = 10
    GameAll = 11
    GameAllies = 12
    GameSpectator = 13
    Cafe = 15
    CustomGame = 16
    Private = 17
    PostGame = 18
    BattleCup = 19
    HLTVSpectator = 20
    GameEvents = 21
    Trivia = 22


class EProfileCardSlotType(betterproto.Enum):
    Empty = 0
    Stat = 1
    Trophy = 2
    Item = 3
    Hero = 4
    Emoticon = 5
    Team = 6


class EMatchGroupServerStatus(betterproto.Enum):
    OK = 0
    LimitedAvailability = 1
    Offline = 2


class DOTACMPick(betterproto.Enum):
    Random = 0
    GoodGuys = 1
    BadGuys = 2


class DOTALowPriorityBanType(betterproto.Enum):
    Abandon = 0
    Reports = 1
    SecondaryAbandon = 2
    PreGameRole = 3


class DOTALobbyReadyState(betterproto.Enum):
    Undeclared = 0
    Accepted = 1
    Declined = 2


class DOTAGameVersion(betterproto.Enum):
    Current = 0
    Stable = 1


class DOTAJoinLobbyResult(betterproto.Enum):
    Success = 0
    AlreadyInGame = 1
    InvalidLobby = 2
    IncorrectPassword = 3
    AccessDenied = 4
    GenericError = 5
    IncorrectVersion = 6
    InTeamParty = 7
    NoLobbyFound = 8
    LobbyFull = 9
    CustomGameIncorrectVersion = 10
    Timeout = 11
    CustomGameCooldown = 12
    Busy = 13
    NoPlaytime = 14


class DOTASelectionPriorityRules(betterproto.Enum):
    Manual = 0
    Automatic = 1


class DOTASelectionPriorityChoice(betterproto.Enum):
    Invalid = 0
    FirstPick = 1
    SecondPick = 2
    Radiant = 3
    Dire = 4


class DOTAMatchVote(betterproto.Enum):
    Invalid = 0
    Positive = 1
    Negative = 2


class DOTALobbyVisibility(betterproto.Enum):
    Public = 0
    Friends = 1
    Unlisted = 2


class EDOTAPlayerMMRType(betterproto.Enum):
    Invalid = 0
    GeneralHidden = 1
    GeneralCompetitive = 3
    SoloCompetitive2019 = 4
    _1v1Competitive_UNUSED = 5
    GeneralSeasonalRanked = 6
    SoloSeasonalRanked = 7
    Competitive_Core = 8
    Competitive_Support = 9
    Competitive_Classic = 10


class EDOTAMMRBoostType(betterproto.Enum):
    NONE = 0
    Leader = 1
    Follower = 2


class MatchType(betterproto.Enum):
    Casual = 0
    CoopBots = 1
    LegacyTeamRanked = 2
    LegacySoloQueue = 3
    Competitive = 4
    WeekendTourney = 5
    Casual1V1 = 6
    Event = 7
    SeasonalRanked = 8
    LowpriDeprecated = 9
    SteamGroup = 10
    Mutation = 11
    CoachesChallenge = 12
    Gauntlet = 13


class DOTABotDifficulty(betterproto.Enum):
    Passive = 0
    Easy = 1
    Medium = 2
    Hard = 3
    Unfair = 4
    Invalid = 5
    Extra1 = 6
    Extra2 = 7
    Extra3 = 8


class DOTABotMode(betterproto.Enum):
    NONE = 0
    Laning = 1
    Attack = 2
    Roam = 3
    Retreat = 4
    SecretShop = 5
    SideShop = 6
    Rune = 7
    PushTowerTop = 8
    PushTowerMid = 9
    PushTowerBot = 10
    DefendTowerTop = 11
    DefendTowerMid = 12
    DefendTowerBot = 13
    Assemble = 14
    AssembleWithHumans = 15
    TeamRoam = 16
    Farm = 17
    DefendAlly = 18
    EvasiveManeuvers = 19
    Roshan = 20
    Item = 21
    Ward = 22
    Companion = 23
    TutorialBoss = 24
    Minion = 25


class MatchLanguages(betterproto.Enum):
    Invalid = 0
    English = 1
    Russian = 2
    Chinese = 3
    Korean = 4
    Spanish = 5
    Portuguese = 6
    English2 = 7


class ETourneyQueueDeadlineState(betterproto.Enum):
    Normal = 0
    Missed = 1
    ExpiredOK = 2
    SeekingBye = 3
    EligibleForRefund = 4
    NA = -1
    ExpiringSoon = 101


class EMatchOutcome(betterproto.Enum):
    Unknown = 0
    RadVictory = 2
    DireVictory = 3
    NotScored_PoorNetworkConditions = 64
    NotScored_Leaver = 65
    NotScored_ServerCrash = 66
    NotScored_NeverStarted = 67
    NotScored_Canceled = 68
    NotScored_Suspicious = 69


class ELaneType(betterproto.Enum):
    Unknown = 0
    Safe = 1
    Off = 2
    Mid = 3
    Jungle = 4
    Roam = 5


class EBadgeType(betterproto.Enum):
    TI7Midweek = 1
    TI7Finals = 2
    TI7AllEvent = 3
    TI8Midweek = 4
    TI8Finals = 5
    TI8AllEvent = 6


class ELeagueStatus(betterproto.Enum):
    Unset = 0
    Unsubmitted = 1
    Submitted = 2
    Accepted = 3
    Rejected = 4
    Concluded = 5
    Deleted = 6


class ELeagueRegion(betterproto.Enum):
    Unset = 0
    NA = 1
    SA = 2
    Europe = 3
    CIS = 4
    China = 5
    Sea = 6


class ELeagueTier(betterproto.Enum):
    Unset = 0
    Amateur = 1
    Professional = 2
    Minor = 3
    Major = 4
    International = 5
    DpcQualifier = 6


class ELeagueTierCategory(betterproto.Enum):
    CategoryAmateur = 1
    CategoryProfessional = 2
    CategoryDpc = 3


class ELeagueFlags(betterproto.Enum):
    FlagsNone = 0
    AcceptedAgreement = 1
    PaymentEmailSent = 2
    CompendiumAllowed = 4
    CompendiumPublic = 8


class ELeagueBroadcastProvider(betterproto.Enum):
    Unknown = 0
    Steam = 1
    Twitch = 2
    Youtube = 3
    Other = 100


class ELeaguePhase(betterproto.Enum):
    Unset = 0
    RegionalQualifier = 1
    GroupStage = 2
    MainEvent = 3


class ELeagueAuditAction(betterproto.Enum):
    Invalid = 0
    LeagueCreate = 1
    LeagueEdit = 2
    LeagueDelete = 3
    LeagueAdminAdd = 4
    LeagueAdminRevoke = 5
    LeagueAdminPromote = 6
    LeagueStreamAdd = 7
    LeagueStreamRemove = 8
    LeagueImageUpdated = 9
    LeagueMessageAdded = 10
    LeagueSubmitted = 11
    LeagueSetPrizePool = 12
    LeagueAddPrizePoolItem = 13
    LeagueRemovePrizePoolItem = 14
    LeagueMatchStart = 15
    LeagueMatchEnd = 16
    LeagueAddInvitedTeam = 17
    LeagueRemoveInvitedTeam = 18
    LeagueStatusChanged = 19
    LeagueStreamEdit = 20
    NodegroupCreate = 100
    NodegroupDestroy = 101
    NodegroupAddTeam = 102
    NodegroupRemoveTeam = 103
    NodegroupSetAdvancing = 104
    NodegroupEdit = 105
    NodegroupPopulate = 106
    NodegroupCompleted = 107
    NodegroupSetSecondaryAdvancing = 108
    NodegroupSetTertiaryAdvancing = 109
    NodeCreate = 200
    NodeDestroy = 201
    NodeAutocreate = 202
    NodeSetTeam = 203
    NodeSetSeriesId = 204
    NodeSetAdvancing = 205
    NodeSetTime = 206
    NodeMatchCompleted = 207
    NodeCompleted = 208
    NodeEdit = 209


class DOTACombatLogTypes(betterproto.Enum):
    Invalid = -1
    Damage = 0
    Heal = 1
    ModifierAdd = 2
    ModifierRemove = 3
    Death = 4
    Ability = 5
    Item = 6
    Location = 7
    Gold = 8
    GameState = 9
    Xp = 10
    Purchase = 11
    Buyback = 12
    AbilityTrigger = 13
    Playerstats = 14
    Multikill = 15
    Killstreak = 16
    TeamBuildingKill = 17
    FirstBlood = 18
    ModifierStackEvent = 19
    NeutralCampStack = 20
    PickupRune = 21
    RevealedInvisible = 22
    HeroSaved = 23
    ManaRestored = 24
    HeroLevelup = 25
    BottleHealAlly = 26
    EndgameStats = 27
    InterruptChannel = 28
    AlliedGold = 29
    AegisTaken = 30
    ManaDamage = 31
    PhysicalDamagePrevented = 32
    UnitSummoned = 33
    AttackEvade = 34
    TreeCut = 35
    SuccessfulScan = 36
    EndKillstreak = 37
    BloodstoneCharge = 38
    CriticalDamage = 39
    SpellAbsorb = 40
    UnitTeleported = 41
    KillEaterEvent = 42


class EDPCFavoriteType(betterproto.Enum):
    All = 0
    Player = 1
    Team = 2
    League = 3


class EDPCPushNotification(betterproto.Enum):
    MatchStarting = 1
    PlayerLeftTeam = 10
    PlayerJoinedTeam = 11
    LeagueResult = 20
    PredictionMatchesAvailable = 30
    PredictionResult = 31
    FantasyPlayerCleared = 40
    FantasyDailySummary = 41
    FantasyFinalResults = 42


class EEventActionScoreMode(betterproto.Enum):
    Add = 0
    Min = 1


@dataclass
class CDOTAClientHardwareSpecs(betterproto.Message):
    logical_processors: int = betterproto.uint32_field(1)
    cpu_cycles_per_second: float = betterproto.fixed64_field(2)
    total_physical_memory: float = betterproto.fixed64_field(3)
    is_64_bit_os: bool = betterproto.bool_field(4)
    upload_measurement: int = betterproto.uint64_field(5)
    prefer_not_host: bool = betterproto.bool_field(6)


@dataclass
class CDOTASaveGame(betterproto.Message):
    match_id: int = betterproto.uint64_field(5)
    save_time: int = betterproto.uint32_field(2)
    players: List["CDOTASaveGamePlayer"] = betterproto.message_field(3)
    save_instances: List["CDOTASaveGameSaveInstance"] = betterproto.message_field(4)


@dataclass
class CDOTASaveGamePlayer(betterproto.Message):
    team: "DOTA_GC_TEAM" = betterproto.enum_field(1)
    name: str = betterproto.string_field(2)
    hero: str = betterproto.string_field(3)


@dataclass
class CDOTASaveGameSaveInstance(betterproto.Message):
    game_time: int = betterproto.uint32_field(2)
    team1_score: int = betterproto.uint32_field(3)
    team2_score: int = betterproto.uint32_field(4)
    player_positions: List[
        "CDOTASaveGameSaveInstancePlayerPositions"
    ] = betterproto.message_field(5)
    save_id: int = betterproto.uint32_field(6)
    save_time: int = betterproto.uint32_field(7)


@dataclass
class CDOTASaveGameCDOTASaveGameSaveInstancePlayerPositions(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)


@dataclass
class CMsgDOTACombatLogEntry(betterproto.Message):
    type: "DOTACombatLogTypes" = betterproto.enum_field(1)
    target_name: int = betterproto.uint32_field(2)
    target_source_name: int = betterproto.uint32_field(3)
    attacker_name: int = betterproto.uint32_field(4)
    damage_source_name: int = betterproto.uint32_field(5)
    inflictor_name: int = betterproto.uint32_field(6)
    is_attacker_illusion: bool = betterproto.bool_field(7)
    is_attacker_hero: bool = betterproto.bool_field(8)
    is_target_illusion: bool = betterproto.bool_field(9)
    is_target_hero: bool = betterproto.bool_field(10)
    is_visible_radiant: bool = betterproto.bool_field(11)
    is_visible_dire: bool = betterproto.bool_field(12)
    value: int = betterproto.uint32_field(13)
    health: int = betterproto.int32_field(14)
    timestamp: float = betterproto.float_field(15)
    stun_duration: float = betterproto.float_field(16)
    slow_duration: float = betterproto.float_field(17)
    is_ability_toggle_on: bool = betterproto.bool_field(18)
    is_ability_toggle_off: bool = betterproto.bool_field(19)
    ability_level: int = betterproto.uint32_field(20)
    location_x: float = betterproto.float_field(21)
    location_y: float = betterproto.float_field(22)
    gold_reason: int = betterproto.uint32_field(23)
    timestamp_raw: float = betterproto.float_field(24)
    modifier_duration: float = betterproto.float_field(25)
    xp_reason: int = betterproto.uint32_field(26)
    last_hits: int = betterproto.uint32_field(27)
    attacker_team: int = betterproto.uint32_field(28)
    target_team: int = betterproto.uint32_field(29)
    obs_wards_placed: int = betterproto.uint32_field(30)
    assist_player0: int = betterproto.uint32_field(31)
    assist_player1: int = betterproto.uint32_field(32)
    assist_player2: int = betterproto.uint32_field(33)
    assist_player3: int = betterproto.uint32_field(34)
    stack_count: int = betterproto.uint32_field(35)
    hidden_modifier: bool = betterproto.bool_field(36)
    is_target_building: bool = betterproto.bool_field(37)
    neutral_camp_type: int = betterproto.uint32_field(38)
    rune_type: int = betterproto.uint32_field(39)
    assist_players: List[int] = betterproto.uint32_field(40)
    is_heal_save: bool = betterproto.bool_field(41)
    is_ultimate_ability: bool = betterproto.bool_field(42)
    attacker_hero_level: int = betterproto.uint32_field(43)
    target_hero_level: int = betterproto.uint32_field(44)
    xpm: int = betterproto.uint32_field(45)
    gpm: int = betterproto.uint32_field(46)
    event_location: int = betterproto.uint32_field(47)
    target_is_self: bool = betterproto.bool_field(48)
    damage_type: int = betterproto.uint32_field(49)
    invisibility_modifier: bool = betterproto.bool_field(50)
    damage_category: int = betterproto.uint32_field(51)
    networth: int = betterproto.uint32_field(52)
    building_type: int = betterproto.uint32_field(53)
    modifier_elapsed_duration: float = betterproto.float_field(54)
    silence_modifier: bool = betterproto.bool_field(55)
    heal_from_lifesteal: bool = betterproto.bool_field(56)
    modifier_purged: bool = betterproto.bool_field(57)
    spell_evaded: bool = betterproto.bool_field(58)
    motion_controller_modifier: bool = betterproto.bool_field(59)
    long_range_kill: bool = betterproto.bool_field(60)
    modifier_purge_ability: int = betterproto.uint32_field(61)
    modifier_purge_npc: int = betterproto.uint32_field(62)
    root_modifier: bool = betterproto.bool_field(63)
    total_unit_death_count: int = betterproto.uint32_field(64)
    aura_modifier: bool = betterproto.bool_field(65)
    armor_debuff_modifier: bool = betterproto.bool_field(66)
    no_physical_damage_modifier: bool = betterproto.bool_field(67)
    modifier_ability: int = betterproto.uint32_field(68)
    modifier_hidden: bool = betterproto.bool_field(69)
    inflictor_is_stolen_ability: bool = betterproto.bool_field(70)
    kill_eater_event: int = betterproto.uint32_field(71)
    unit_status_label: int = betterproto.uint32_field(72)
    spell_generated_attack: bool = betterproto.bool_field(73)
    at_night_time: bool = betterproto.bool_field(74)
    attacker_has_scepter: bool = betterproto.bool_field(75)


@dataclass
class CMsgPendingEventAward(betterproto.Message):
    event_id: "EEvent" = betterproto.enum_field(1)
    action_id: int = betterproto.uint32_field(2)
    num_to_grant: int = betterproto.uint32_field(3)
    score_mode: "EEventActionScoreMode" = betterproto.enum_field(4)
    audit_action: int = betterproto.uint32_field(5)
