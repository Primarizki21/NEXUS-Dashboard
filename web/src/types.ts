export interface NationalSummary {
  tpt_2024: number;
  tpt_2023: number;
  tpt_change: number;
  underemployed_2024_juta: number;
  underemployed_2023_juta: number;
  underemployed_growth_pct: number;
  lu2_2024: number;
  lu2_2023: number;
  lu2_change: number;
  youth_tpt: number;
  adult_tpt: number;
  youth_vulnerability_ratio: number;
  youth_share_of_unemployed: number;
  smk_tpt: number;
  sd_tpt: number;
  univ_tpt: number;
  educated_disparity_ratio: number;
  moran_i_2024: number;
  moran_p_value: number;
  sdm_r2: number;
  ols_r2: number;
  wage_spillover_multiplier: number;
  wage_direct_effect: number;
  rpjmn_target_tpt_2029: number;
  forecast_tpt_2030: number;
  total_job_target: number;
}

export interface Province {
  name: string;
  pulau: string;
  lat: number;
  lon: number;
  tpt: number;
  tpt_laki: number;
  tpt_puan: number;
  gender_gap: number;
  informal: number;
  formal: number;
  upah: number;
  mismatch: number;
  cluster_id: number;
  cluster_name: string;
  lisa_quad: string;
  lisa_sig: boolean;
  ikkd_score: number;
}

export interface ClusterProfile {
  id: number;
  name: string;
  tagline: string;
  tpt_mean: number;
  formal_mean: number;
  upah_mean: number;
  color: string;
  desc: string;
  policy: string;
  target_jobs: number;
  provinces: string[];
}

export interface SpatialModel {
  model: string;
  params: number;
  loglik: number;
  aic: number;
  spatial_lag: string;
  r2: number;
  status: string;
}

export interface LeSagePaceItem {
  variable: string;
  domestic_coef: number;
  spatial_coef: number;
  direct_effect: number;
  spillover_effect: number;
  total_effect: number;
  multiplier: number;
}

export interface MoranYear {
  year: number;
  moran_i: number;
  expected_i: number;
  p_value: number;
  status: string;
  significant: boolean;
}

export interface ForecastPoint {
  year: number;
  tpt: number;
  lower_80: number;
  upper_80: number;
  lower_95: number;
  upper_95: number;
  type: string;
}

export interface HistoricalPoint {
  year: number;
  tpt: number;
  type: string;
}

export interface LaborUtilizationItem {
  category: string;
  amount_2023_juta: number;
  amount_2024_juta: number;
  change_juta: number;
  pct_2023: number;
  pct_2024: number;
}

export interface EducationLadderItem {
  education: string;
  tpt_2022: number;
  tpt_2023: number;
  tpt_2024: number;
}

export interface UrbanRuralItem {
  indicator: string;
  unit: string;
  urban: number;
  rural: number;
  disparity_ratio: number;
  property: string;
}

export interface MethodologyVIF {
  variable: string;
  vif: number;
  status: string;
}

export interface LaborDataBundle {
  meta: {
    title: string;
    subtitle: string;
    dataset_source: string;
    benchmark_period: string;
    provinces_count: number;
    clusters_count: number;
  };
  national_summary: NationalSummary;
  clusters: ClusterProfile[];
  provinces: Province[];
  spatial_models: SpatialModel[];
  lesage_pace: LeSagePaceItem[];
  moran_trajectory: MoranYear[];
  historical_trajectory: HistoricalPoint[];
  forecast_trajectory: ForecastPoint[];
  labor_utilization: LaborUtilizationItem[];
  education_ladder: EducationLadderItem[];
  urban_rural: UrbanRuralItem[];
  methodology_vif: MethodologyVIF[];
  methodology_panel: {
    balanced_n: number;
    balanced_t: number;
    total_panel_obs: number;
    between_province_variance_pct: number;
    within_province_variance_pct: number;
    spatial_matrix_type: string;
  };
}
