import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function formatScore(score: number): string {
  return score.toFixed(1);
}

export function scoreColor(score: number): string {
  if (score >= 80) return "text-green-600 dark:text-green-400";
  if (score >= 60) return "text-yellow-600 dark:text-yellow-400";
  if (score >= 40) return "text-orange-600 dark:text-orange-400";
  return "text-red-600 dark:text-red-400";
}

export function scoreBg(score: number): string {
  if (score >= 80) return "bg-green-100 dark:bg-green-950";
  if (score >= 60) return "bg-yellow-100 dark:bg-yellow-950";
  if (score >= 40) return "bg-orange-100 dark:bg-orange-950";
  return "bg-red-100 dark:bg-red-950";
}
